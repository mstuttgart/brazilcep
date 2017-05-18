# -*- coding: utf-8 -*-

import requests
from unittest import mock
from unittest import TestCase
from jinja2 import Environment, PackageLoader

import pycep_correios
from pycep_correios.correios_exceptions import \
    CorreiosCEPInvalidCEPException
from pycep_correios.correios_exceptions import \
    CorreiosTimeOutException
from pycep_correios.correios_exceptions import \
    CorreiosCEPTooManyRedirectsException
from pycep_correios.correios_exceptions import \
    CorreiosCEPConnectionErrorException


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
            'rua': address['end'],
            'uf': address['uf'],
        }

        self.env = Environment(loader=PackageLoader('test', 'templates'))

        template = self.env.get_template('response.xml')
        xml = template.render(**address)
        self.response_xml = (xml.replace('\n', '')).replace('\t', '')

        template = self.env.get_template('response_error.xml')
        xml = template.render()
        self.response_xml_error = (xml.replace('\n', '')).replace('\t', '')

    @mock.patch('pycep_correios.requests.post')
    def test_get_cep(self, mock_api_call):

        # Aqui realizamos consulta com o CEP correto
        param = {
            'text': self.response_xml,
            'ok': True,
            'status_code': 200,
        }

        mock_api_call.return_value = mock.MagicMock(**param)

        self.assertDictEqual(pycep_correios.get_cep('70002900'),
                             self.expected_address)

        # Aqui realizamos consultas que de alguma forma retornam mensagens de
        # erro
        param = {
            'text': self.response_xml_error,
            'ok': False,
        }

        mock_api_call.return_value = mock.MagicMock(**param)

        self.assertRaises(CorreiosCEPInvalidCEPException,
                          pycep_correios.get_cep, '1232710')

        mock_api_call.side_effect = requests.exceptions.Timeout()
        self.assertRaises(CorreiosTimeOutException,
                          pycep_correios.get_cep, '12345-500')

        mock_api_call.side_effect = requests.exceptions.Timeout()
        self.assertRaises(CorreiosTimeOutException,
                          pycep_correios.get_cep, '12345-500')

        mock_api_call.side_effect = requests.exceptions.TooManyRedirects()
        self.assertRaises(CorreiosCEPTooManyRedirectsException,
                          pycep_correios.get_cep, '12345-500')

        mock_api_call.side_effect = requests.exceptions.ConnectionError()
        self.assertRaises(CorreiosCEPConnectionErrorException,
                          pycep_correios.get_cep, '12345-500')

    def test__format_cep(self):
        self.assertRaises(CorreiosCEPInvalidCEPException,
                          pycep_correios._format_cep, 37503003)

    def test__mount_request(self):
        cep = '37503005'
        template = self.env.get_template('consultacep.xml')
        xml = template.render(cep=cep)
        xml = (xml.replace('\n', '')).replace('\t', '')

        self.assertEqual(xml, pycep_correios._mount_request(cep=cep))

    def test__parse_response(self):
        response = pycep_correios._parse_response(self.response_xml)
        self.assertDictEqual(response, self.expected_address)

    def test__parse_error(self):
        fault = pycep_correios._parse_error(self.response_xml_error)
        self.assertEqual(fault.strip(), 'BUSCA DEFINIDA COMO EXATA, '
                                        '0 CEP DEVE TER 8 DIGITOS')
