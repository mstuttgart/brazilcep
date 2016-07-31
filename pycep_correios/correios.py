# -*- coding: utf-8 -*-
# #############################################################################
# The MIT License (MIT)
#
# Copyright (c) 2016 Michell Stuttgart
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# #############################################################################

import xml.etree.cElementTree as Et
import requests

from pycep_correios.correios_exceptions import CorreiosCEPConnectionErrorException
from pycep_correios.correios_exceptions import CorreiosCEPInvalidCEPException
from pycep_correios.correios_exceptions import CorreiosTimeOutException
from pycep_correios.correios_exceptions import CorreiosCEPTooManyRedirectsException
from pycep_correios.correios_exceptions import CorreiosCEPHTTPErrorException


class Correios(object):

    URL = 'https://apps.correios.com.br/SigepMasterJPA' \
              '/AtendeClienteService/AtendeCliente?wsdl'

    HEADER = '<soap:Envelope ' \
             'xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\" ' \
             'xmlns:cli=\"http://cliente.bean.master.sigep.bsb.correios.com' \
             '.br/\"><soap:Header/><soap:Body>'

    FOOTER = '</soap:Body></soap:Envelope>'

    @staticmethod
    def get_cep(cep: str):

        try:
            cep = cep.replace('-', '')
            cep = cep.replace('.', '')
        except AttributeError:
            raise CorreiosCEPInvalidCEPException('[ERRO] CEP deve ser do tipo string, '
                                                 'mas o tipo encontrado foi %s!' % type(cep))

        xml = Correios._mount_request(cep)

        try:
            response = requests.post(Correios.URL,
                                     data=xml,
                                     headers={'Content-type': 'text/xml'},
                                     verify=False)

        except requests.exceptions.Timeout as e:
            raise CorreiosTimeOutException(str(e))

        except requests.exceptions.TooManyRedirects as e:
            raise CorreiosCEPTooManyRedirectsException(str(e))

        except requests.exceptions.HTTPError as e:
            raise CorreiosCEPHTTPErrorException(str(e))

        except requests.ConnectionError as e:
            raise CorreiosCEPConnectionErrorException(str(e))
        else:

            if not response.ok:
                msg = Correios._parse_error(response.text)
                raise CorreiosCEPInvalidCEPException(msg)

            address_data = Correios._parse_response(response.text)
            return address_data

    @staticmethod
    def _mount_request(cep):

        xml = Correios.HEADER
        xml += '<cli:consultaCEP>'
        xml += '<cep>%s</cep>' % cep
        xml += '</cli:consultaCEP>'
        xml += Correios.FOOTER
        return xml

    @staticmethod
    def _parse_response(xml):

        end = Et.fromstring(xml).find('.//return')

        response = {
            'rua': end.findtext('end'),
            'bairro': end.findtext('bairro'),
            'cidade': end.findtext('cidade'),
            'uf': end.findtext('uf'),
            'complemento': end.findtext('complemento'),
            'outro': end.findtext('complemento2')
        }

        return response

    @staticmethod
    def _parse_error(xml):
        return Et.fromstring(xml).findtext('.//faultstring')
