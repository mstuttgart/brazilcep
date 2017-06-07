#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pycep_correios
----------------------------------

Tests for `pycep_correios` module.
"""

import requests
from unittest import mock, TestCase
from jinja2 import Environment, PackageLoader

from pycep_correios import get_address, format_cep, validate_cep
from pycep_correios import parser
from pycep_correios.exceptions import InvalidCEP


class TestCorreios(TestCase):

    def setUp(self):

        address = {
            'bairro': 'Asa Norte',
            'cep': '70002900',
            'cidade': 'Brasília',
            'end': 'SBN Quadra 1 Bloco A',
            'id': '0',
            'uf': 'DF',
        }

        self.expected_address = {
            'bairro': address['bairro'],
            'cidade': address['cidade'],
            'complemento': '',
            'outro': '',
            'logradouro': address['end'],
            'uf': address['uf'],
        }

        self.env = Environment(loader=PackageLoader('tests', 'templates'))

        template = self.env.get_template('response.xml')
        xml = template.render(**address)
        self.response_xml = (xml.replace('\n', '')).replace('\t', '')

        template = self.env.get_template('response_error.xml')
        xml = template.render()
        self.response_xml_error = (xml.replace('\n', '')).replace('\t', '')

    @mock.patch('requests.post')
    def test_get_address(self, mock_api_call):

        # Aqui realizamos consulta com o CEP correto
        param = {
            'text': self.response_xml,
            'ok': True,
            'status_code': 200,
        }

        mock_api_call.return_value = mock.MagicMock(**param)

        self.assertDictEqual(get_address('70002900'), self.expected_address)

        # Aqui realizamos consultas que de alguma forma retornam mensagens de
        # erro
        param = {
            'text': self.response_xml_error,
            'ok': False,
        }

        mock_api_call.return_value = mock.MagicMock(**param)

        self.assertRaises(InvalidCEP, get_address, '1232710')

    def test_format_cep(self):
        self.assertRaises(AttributeError, format_cep, 37503003)
        self.assertEqual(format_cep('37.503-003'), '37503003')

    def test_validate_cep(self):
        self.assertRaises(AttributeError, validate_cep, 37503003)
        self.assertIs(validate_cep('37.503-003'), True)
        self.assertIs(validate_cep('37.503-00'), False)

    def test_mount_request(self):
        template = self.env.get_template('consultacep.xml')
        xml = template.render(cep='37503005')
        xml = (xml.replace('\n', '')).replace('\t', '')

        self.assertEqual(xml, parser.mount_request(cep='37503005'))

    def test_parse_response(self):
        response = parser.parse_response(self.response_xml)
        self.assertDictEqual(response, self.expected_address)

    def test_parse_error_response(self):
        fault = parser.parse_error_response(self.response_xml_error)
        self.assertEqual(fault.strip(), 'BUSCA DEFINIDA COMO EXATA, '
                                        '0 CEP DEVE TER 8 DIGITOS')
