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
from jinja2 import Environment, FileSystemLoader

from .correios_exceptions import CorreiosCEPConnectionErrorException
from .correios_exceptions import CorreiosCEPInvalidCEPException
from .correios_exceptions import CorreiosTimeOutException
from .correios_exceptions import CorreiosCEPTooManyRedirectsException


class Correios:

    URL = 'https://apps.correios.com.br/SigepMasterJPA' \
              '/AtendeClienteService/AtendeCliente?wsdl'

    @staticmethod
    def get_cep(cep: str) -> dict:

        """
        Retorna dos dados do endereço de um dado cep, a saber:
        rua: logradouro do cep
        bairro: bairro do cep
        cidade: cidade do cep
        uf: Abreviacao do estado do cep
        complementento: informações adicionais sobre o cep
        outro: informações variadas sobre o cep como por exemplo o intervalo
        de numero de residência que o mesmo compreende.

        :param cep: string contendo o cep a ser consultado
        :return: dict contendo os dados do endereço do cep consultado.
        """

        xml = Correios._mount_request(Correios._format_cep(cep))

        try:
            response = requests.post(Correios.URL,
                                     data=xml,
                                     headers={'Content-type': 'text/xml'},
                                     verify=False)

        except requests.exceptions.Timeout:
            raise CorreiosTimeOutException('Connection Timeout, please retry later')

        except requests.exceptions.TooManyRedirects:
            raise CorreiosCEPTooManyRedirectsException('Bad URL, check the formatting '
                                                       'of your request and try again')

        except requests.ConnectionError:
            raise CorreiosCEPConnectionErrorException('Could not connect to the API. '
                                                      'Please check your connection')
        else:

            if not response.ok:

                msg = Correios._parse_error(response.text)
                raise CorreiosCEPInvalidCEPException(msg)

            return Correios._parse_response(response.text)

    @staticmethod
    def _format_cep(cep):

        try:
            cep = cep.replace('-', '')
            cep = cep.replace('.', '')
        except AttributeError:
            raise CorreiosCEPInvalidCEPException('CEP deve ser do tipo string, '
                                                 'mas o tipo encontrado foi %s!' % type(cep))

        return cep

    @staticmethod
    def _mount_request(cep):

        env = Environment(loader=FileSystemLoader('pycep_correios/templates'))
        template = env.get_template('consultacep.xml')
        xml = template.render(cep=cep)
        return (xml.replace("\n","")).replace("\t","")

    @staticmethod
    def _parse_response(xml):

        end = Et.fromstring(xml).find('.//return')

        address = {
            'rua': end.findtext('end'),
            'bairro': end.findtext('bairro'),
            'cidade': end.findtext('cidade'),
            'uf': end.findtext('uf'),
            'complemento': end.findtext('complemento'),
            'outro': end.findtext('complemento2')
        }

        return address

    @staticmethod
    def _parse_error(xml):
        return Et.fromstring(xml).findtext('.//faultstring')
