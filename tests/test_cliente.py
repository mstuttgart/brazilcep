#!/usr/bin/env python
# -*- coding: utf-8 -*-

from unittest import mock, TestCase
from jinja2 import Environment, PackageLoader

from pycep_correios import consultar_cep, formatar_cep, validar_cep
from pycep_correios import parser
from pycep_correios.excecoes import CEPInvalido


class TestCorreios(TestCase):

    def setUp(self):

        self.expected_address = {
            'bairro': 'Santo Antônio',
            'cep': '37503130',
            'cidade': 'Itajubá',
            'end': 'Rua Geraldino Campista',
            'id': '0',
            'uf': 'MG',
            'complemento': '',
            'complemento2': '- até 214/215',
        }

        self.env = Environment(loader=PackageLoader('tests', 'templates'))

        template = self.env.get_template('resposta.xml')
        xml = template.render(**self.expected_address)
        self.response_xml = (xml.replace('\n', '')).replace('\t', '')

        template = self.env.get_template('resposta_error.xml')
        xml = template.render()
        self.response_xml_error = (xml.replace('\n', '')).replace('\t', '')

    @mock.patch('requests.post')
    def test_consultar_cep(self, mock_api_call):

        # Criamos uma requisicao que sera bem sucedida
        param = {
            'text': self.response_xml,
            'ok': True,
            'status_code': 200,
        }

        mock_api_call.return_value = mock.MagicMock(**param)

        self.assertDictEqual(consultar_cep('70002900'), self.expected_address)

        # Aqui, construímos uma requisição que retornará erro
        param = {
            'text': self.response_xml_error,
            'ok': False,
        }

        mock_api_call.return_value = mock.MagicMock(**param)
        self.assertRaises(CEPInvalido, consultar_cep, '1232710')

        mock_api_call.return_value = mock.MagicMock(**param)
        self.assertRaises(CEPInvalido, consultar_cep, '00000000')

    def test_formatar_cep(self):
        self.assertRaises(AttributeError, formatar_cep, 37503003)
        self.assertEqual(formatar_cep('37.503-003'), '37503003')

    def test_validar_cep(self):
        self.assertRaises(AttributeError, validar_cep, 37503003)
        self.assertIs(validar_cep('37.503-003'), True)
        self.assertIs(validar_cep('37.503-00'), False)

    def test_monta_requisicao(self):
        template = self.env.get_template('consultacep.xml')
        xml = template.render(cep='37503005')
        xml = (xml.replace('\n', '')).replace('\t', '')

        self.assertEqual(xml, parser.monta_requisicao(cep='37503005'))

    def test_parse_resposta(self):
        response = parser.parse_resposta(self.response_xml)
        self.assertDictEqual(response, self.expected_address)

    def test_parse_resposta_com_erro(self):
        fault = parser.parse_resposta_com_erro(self.response_xml_error)
        self.assertEqual(fault.strip(), 'BUSCA DEFINIDA COMO EXATA, '
                                        '0 CEP DEVE TER 8 DIGITOS')
