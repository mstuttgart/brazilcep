# -*- coding: utf-8 -*-
# #############################################################################
#   Copyright (C) 2015  Michell Stuttgart
#   This program is free software: you can redistribute it and/or modify it
#   under the terms of the GNU General Public License as published by the Free
#   Software Foundation, either version 3 of the License, or (at your option)
#   any later version.
#   This program is distributed in the hope that it will be useful, but WITHOUT
#   ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#   FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#   more details.
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


class CorreiosCEP(object):

    @staticmethod
    def get_cep(cep):

        url = 'https://apps.correios.com.br/SigepMasterJPA' \
              '/AtendeClienteService/AtendeCliente?wsdl'

        try:
            service = client.Client(url).service
        except client.TransportError as e:
            raise e.message

        try:
            cep = service.consultaCEP(cep)
        except WebFault as e:
            raise e.message

        cep_dict = {
            'cep': str(cep.cep),
            'bairro': str(cep.bairro.encode('utf8')) if cep.bairro else '',
            'cidade': str(cep.cidade.encode('utf8')) if cep.cidade else '',
            'complemento': str(
                cep.complemento.encode('utf8')) if cep.complemento else '',
            'complemento2': str(
                cep.complemento2.encode('utf8')) if cep.complemento2 else '',
            'rua': str(cep.end.encode('utf8')) if cep.end else '',
            'id': cep.id,
            'UF': str('res.uf'),
        }

        return cep_dict


res = CorreiosCEP().get_cep('37503130')
print res
