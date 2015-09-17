# -*- coding: utf-8 -*-
# #############################################################################
#   Copyright (C) 2015  Michell Stuttgart
#
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the Free
#   Software Foundation, either version 3 of the License, or (at your option)
#   any later version.
#
#   This program is distributed in the hope that it will be useful, but WITHOUT
#   ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#   FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#   more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# #############################################################################

try:
    from suds import client
    from suds import WebFault
except ImportError:
    raise (ImportError, 'Python module suds not installed. '
                        'Please install with: pip install suds')

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
