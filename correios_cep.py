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
except ImportError as exp:
    print exp.message
    print 'Python module suds not installed. ' \
          'Please install with: pip install suds'

from correios_cep_exceptions import CorreiosCEPExceptions


class EnderecoCEP(object):

    def __init__(self, cep='00000000', rua='', bairro='', complemento='',
                 complemento2='', cidade='', UF=''):
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.complemento = complemento
        self.complemento2 = complemento2
        self.cidade = cidade
        self.UF = UF


class CorreiosCEP(object):

    @staticmethod
    def get_cep(cep):

        if not isinstance(cep, str):
            raise CorreiosCEPExceptions(u'CEP não é uma string')

        cep = (cep.replace('-', '')).replace('.', '')

        url = 'https://apps.correios.com.br/SigepMasterJPA' \
              '/AtendeClienteService/AtendeCliente?wsdl'

        try:
            service = client.Client(url).service
        except client.TransportError as e:
            raise CorreiosCEPExceptions(e.message)

        try:
            res_cep = service.consultaCEP(cep)
        except WebFault as e:
            raise CorreiosCEPExceptions(e.message)

        end_obj = EnderecoCEP()
        end_obj.cep = str(res_cep.cep)
        end_obj.rua = str(res_cep.end.encode('utf8')) if res_cep.end else ''
        end_obj.bairro = str(res_cep.bairro.encode('utf8')) if res_cep.bairro else ''
        end_obj.cidade = str(res_cep.cidade.encode('utf8')) if res_cep.cidade else ''
        end_obj.UF = str(res_cep.uf)
        end_obj.complemento = str(
            res_cep.complemento.encode('utf8')) if res_cep.complemento else ''
        end_obj.complemento2 = str(
                res_cep.complemento2.encode('utf8')) if res_cep.complemento2 else ''

        return end_obj
