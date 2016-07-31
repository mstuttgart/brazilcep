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

from pycep_correios.correios import Correios
from pycep_correios.correios_exceptions import \
    CorreiosCEPInvalidCEPException


class TestCorreios(unittest.TestCase):

    def test_get_cep(self):

        address = {
            'bairro': 'Santo Antônio',
            'cidade': 'Itajubá',
            'complemento': '',
            'outro': '- até 214/215',
            'rua': 'Rua Geraldino Campista',
            'uf': 'MG',
        }

        self.assertDictEqual(address, Correios.get_cep('37.503-130'))

        self.assertRaises(CorreiosCEPInvalidCEPException,
                          Correios.get_cep, '1232710')

        self.assertRaises(CorreiosCEPInvalidCEPException,
                          Correios.get_cep, '00000-000')

        self.assertRaises(CorreiosCEPInvalidCEPException,
                          Correios.get_cep, 37503003)

    def test__mount_request(self):

        xml = Correios.HEADER
        xml += '<cli:consultaCEP>'
        xml += '<cep>%s</cep>' % '37503005'
        xml += '</cli:consultaCEP>'
        xml += Correios.FOOTER

        self.assertEqual(xml, Correios._mount_request('37503005'))

    def test__parse_response(self):

        xml = '''<S:Envelope
                xmlns:S=\"http://schemas.xmlsoap.org/soap/envelope/\">
                <S:Body>
                <ns2:consultaCEPResponse
                xmlns:ns2=\"http://cliente.bean.master.sigep.bsb.correios.com.br/\">
                    <return>
                        <bairro>Asa Norte</bairro>
                        <cep>70002900</cep>
                        <cidade>Brasília</cidade>
                        <complemento/>
                        <complemento2/>
                        <end>SBN Quadra 1 Bloco A</end>
                        <id>0</id>
                        <uf>DF</uf>
                    </return>
                </ns2:consultaCEPResponse>
                </S:Body>
                </S:Envelope>'''.replace('\n', '')

        response = Correios._parse_response(xml)

        self.assertEqual(response['rua'], 'SBN Quadra 1 Bloco A')
        self.assertEqual(response['bairro'], 'Asa Norte')
        self.assertEqual(response['cidade'], 'Brasília')
        self.assertEqual(response['uf'], 'DF')
        self.assertEqual(response['complemento'], '')
        self.assertEqual(response['outro'], '')

    def test__parse_error(self):

        xml = '''<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body><soap:Fault>
        <faultcode>soap:Server</faultcode>
        <faultstring>BUSCA DEFINIDA COMO EXATA, 0 CEP DEVE TER 8 DIGITOS</faultstring>
        <detail><ns2:SigepClienteException xmlns:ns2="http://cliente.bean.master.sigep.bsb.correios.com.br/">
        BUSCA DEFINIDA COMO EXATA, 0 CEP DEVE TER 8 DIGITOS
        </ns2:SigepClienteException></detail></soap:Fault>
        </soap:Body></soap:Envelope>'''.replace('\n', '')

        fault = Correios._parse_error(xml)
        self.assertEqual(fault, 'BUSCA DEFINIDA COMO EXATA, 0 CEP DEVE TER 8 DIGITOS')
