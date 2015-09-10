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

    def __init__(self, cep='', rua='', bairro='', complemento='',
                 complemento2='', cidade='', UF=''):
        self.cep = cep
        self.rua = rua
        self.bairro = bairro
        self.complemento = complemento
        self.complemento2 = complemento2
        self.cidade = cidade
        self.UF = UF
        self.erro_msg = None


class CorreiosCEP(object):

    def _preenche_endereco(self, cep, rua='', bairro='', complemento='',
                           complemento2='', cidade='', UF='', msg=None):

        obj_end = EnderecoCEP()
        obj_end.cep = cep
        obj_end.rua = rua
        obj_end.bairro = bairro
        obj_end.complemento = complemento
        obj_end.complemento2 = complemento2
        obj_end.cidade = cidade
        obj_end.UF = UF
        obj_end.erro_msg = msg

        return obj_end

    def get_cep(self, cep):

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
            return self._preenche_endereco(cep, msg=e.message)

        cep = str(res_cep.cep)
        rua = str(res_cep.end.encode('utf8')) if res_cep.end else ''
        bairro = str(res_cep.bairro.encode('utf8')) if res_cep.bairro else ''
        cidade = str(res_cep.cidade.encode('utf8')) if res_cep.cidade else ''
        UF = str(res_cep.uf)
        complemento = str(res_cep.complemento.encode('utf8')) if \
            res_cep.complemento else ''
        complemento2 = str(res_cep.complemento2.encode('utf8')) if \
            res_cep.complemento2 else ''

        return self._preenche_endereco(cep, rua=rua, bairro=bairro,
                                       complemento=complemento,
                                       complemento2=complemento2,
                                       cidade=cidade, UF=UF)
