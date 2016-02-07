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
from pycep_correios.pycep_correios import PyCEPCorreios
from pycep_correios.pycep_correios_exceptions import \
    CorreiosCEPInvalidCEPException


class TestPyCEPCorreios(unittest.TestCase):

    def setUp(self):
        self.corr_obj = PyCEPCorreios()

    def test_get_cep(self):
        end_1 = {
            'bairro': 'Santo Antônio',
            'cidade': 'Itajubá',
            'complemento': '',
            'outro': '- até 214/215',
            'rua': 'Rua Geraldino Campista',
            'uf': 'MG',
        }

        self.assertItemsEqual(end_1, self.corr_obj.get_cep('37.503-130'))

        self.assertRaises(CorreiosCEPInvalidCEPException,
                          self.corr_obj.get_cep, '1232710')

        self.assertRaises(CorreiosCEPInvalidCEPException,
                          self.corr_obj.get_cep, '00000-000')

        self.assertRaises(CorreiosCEPInvalidCEPException,
                          self.corr_obj.get_cep, 37503130)