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

from suds import client
from suds import WebFault

from pycep_correios_exceptions import CorreiosCEPServerConnectionException
from pycep_correios_exceptions import CorreiosCEPInvalidCEPException


class PyCEPCorreios(object):

    def _preencher_endereco(self, resposta_servidor):

        endereco = {
            'rua': str(resposta_servidor.end.encode('utf8')) if
            resposta_servidor.end else '',
            'bairro': str(resposta_servidor.bairro.encode('utf8')) if
            resposta_servidor.bairro else '',
            'cidade': str(resposta_servidor.cidade.encode('utf8')) if
            resposta_servidor.cidade else '',
            'uf': str(resposta_servidor.uf),
            'complemento': str(
                resposta_servidor.complemento.encode('utf8')) if
            resposta_servidor.complemento else '',
            'outro': str(resposta_servidor.complemento2.encode('utf8'))
            if resposta_servidor.complemento2 else '',
        }

        return endereco

    def get_cep(self, cep):

        if not isinstance(cep, str):
            raise CorreiosCEPInvalidCEPException(u'O valor de CEP fornecido'
                                                 u'não é uma string')

        cep = (cep.replace('-', '')).replace('.', '')

        url = 'https://apps.correios.com.br/SigepMasterJPA' \
              '/AtendeClienteService/AtendeCliente?wsdl'

        try:
            service = client.Client(url).service
        except client.TransportError as e:
            raise CorreiosCEPServerConnectionException(e.message)

        try:
            res_cep = service.consultaCEP(cep)
        except WebFault as e:
            raise CorreiosCEPInvalidCEPException(e.message)

        return self._preencher_endereco(res_cep)
