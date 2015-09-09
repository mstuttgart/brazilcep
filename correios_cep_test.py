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


class TestCorreiosCEP(unittest.TestCase):

    def setUp(self):

        self.cep_test_1 = {
            'cep': '37503130',
            'bairro': 'Santo Antônio',
            'cidade': 'Itajubá',
            'complemento': '',
            'complemento2': '- até 214/215',
            'rua': 'Rua Geraldino Campista',
            'id': long(0),
            'UF': 'MG',
        }

    def test_get_cep(self):
        cep = CorreiosCEP.get_cep(self.cep_test_1['cep'])

        self.assertIsInstance(cep, dict)
        self.assertDictContainsSubset(cep, self.cep_test_1)


if __name__ == "__main__":
    unittest.main()
