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

import sys
import os
test_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(test_root)
sys.path.insert(0, os.path.dirname(test_root))
sys.path.insert(0, test_root)

import unittest
from pycep_correios.pycep_correios import PyCEPCorreios
from pycep_correios.pycep_correios_exceptions import \
    CorreiosCEPInvalidCEPException


class TestPyCEPCorreios(unittest.TestCase):
    def setUp(self):
        self.corr_obj = PyCEPCorreios()

    def test_get_cep(self):
        end_1 = {
            'Bairro': 'Santo Antônio',
            'Cidade': 'Itajubá',
            'Complemento': '',
            'Outro': '- até 214/215',
            'Rua': 'Rua Geraldino Campista',
            'UF': 'MG',
        }

        self.assertItemsEqual(end_1, self.corr_obj.get_cep('37.503-130'))

        self.assertRaises(CorreiosCEPInvalidCEPException,
                          self.corr_obj.get_cep, '1232710')

        self.assertRaises(CorreiosCEPInvalidCEPException,
                          self.corr_obj.get_cep, '00000-000')

        self.assertRaises(CorreiosCEPInvalidCEPException,
                          self.corr_obj.get_cep, 37503130)


if __name__ == "__main__":
    unittest.main()
