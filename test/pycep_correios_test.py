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
