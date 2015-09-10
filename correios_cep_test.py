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

import unittest
from correios_cep import CorreiosCEP
from correios_cep import EnderecoCEP


class TestCorreiosCEP(unittest.TestCase):
    def setUp(self):
        end_1 = {
            'cep': '37.503-130',
            'bairro': 'Santo Antônio',
            'cidade': 'Itajubá',
            'complemento': '',
            'complemento2': '- até 214/215',
            'rua': 'Rua Geraldino Campista',
            'UF': 'MG',
            'erro_msg': None,
        }

        end_2 = {
            'cep': '12327-130',
            'bairro': 'Centro',
            'cidade': 'Jacareí',
            'complemento': '',
            'complemento2': '',
            'rua': 'Rua Batista Scavone',
            'UF': 'SP',
            'erro_msg': None,
        }

        end_3 = {
            'cep': '12327-10',
            'bairro': '',
            'cidade': '',
            'complemento': '',
            'complemento2': '',
            'rua': '',
            'UF': '',
            'erro_msg': u"Server raised fault: 'BUSCA DEFINIDA COMO EXATA, "
                        u"0 CEP DEVE TER 8 DIGITOS'",
        }

        end_4 = {
            'cep': '37503135',
            'bairro': '',
            'cidade': '',
            'complemento': '',
            'complemento2': '',
            'rua': '',
            'UF': '',
            'erro_msg': u"Server raised fault: 'CEP NAO ENCONTRADO'",
        }

        self.enderecos = [end_1, end_2, end_3, end_4]

    def test_get_cep(self):
        corr_obj = CorreiosCEP()

        for end in self.enderecos:
            endereco = corr_obj.get_cep(end['cep'])
            self.assertIsInstance(endereco, EnderecoCEP)

            cep = (end['cep'].replace('-', '')).replace('.', '')
            self.assertEqual(endereco.cep, cep)
            self.assertEqual(endereco.rua, end['rua'])
            self.assertEqual(endereco.bairro, end['bairro'])
            self.assertEqual(endereco.cidade, end['cidade'])
            self.assertEqual(endereco.UF, end['UF'])
            self.assertEqual(endereco.complemento, end['complemento'])
            self.assertEqual(endereco.complemento2, end['complemento2'])
            self.assertEqual(endereco.erro_msg, end['erro_msg'])


if __name__ == "__main__":
    unittest.main()
