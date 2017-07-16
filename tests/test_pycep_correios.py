# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

import jinja2
import requests

from pycep_correios import consultar_cep, formatar_cep, parser, validar_cep
from pycep_correios import HOMOLOGACAO, PRODUCAO
from pycep_correios.excecoes import (CEPInvalido,
                                     ExcecaoPyCEPCorreios,
                                     Timeout,
                                     MultiploRedirecionamento,
                                     FalhaNaConexao)

try:
    from unittest import mock
except ImportError:
    import mock


class TestPyCEPCorreios(unittest.TestCase):

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

        loader = jinja2.PackageLoader('tests', 'templates')
        self.env = jinja2.Environment(loader=loader)

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
        self.assertDictEqual(consultar_cep('70002900', ambiente=HOMOLOGACAO),
                             self.expected_address)
        self.assertDictEqual(consultar_cep('70002900', ambiente=PRODUCAO),
                             self.expected_address)

        # Aqui, construímos uma requisição que retornará erro
        param = {
            'text': self.response_xml_error,
            'ok': False,
        }

        mock_api_call.return_value = mock.MagicMock(**param)
        self.assertRaises(CEPInvalido, consultar_cep, '1232710')

        mock_api_call.return_value = mock.MagicMock(**param)
        self.assertRaises(CEPInvalido, consultar_cep, '00000000')

        self.assertRaises(KeyError, consultar_cep, '37503130', ambiente=3)

        # Verificamos as demais excecoes
        mock_api_call.side_effect = requests.ConnectTimeout()
        self.assertRaises(Timeout, consultar_cep, '37503130')

        mock_api_call.side_effect = requests.ConnectionError('', '')
        self.assertRaises(FalhaNaConexao, consultar_cep, '37503130')

        mock_api_call.side_effect = requests.TooManyRedirects()
        self.assertRaises(MultiploRedirecionamento, consultar_cep, '37503130')

        mock_api_call.side_effect = requests.RequestException()
        self.assertRaises(ExcecaoPyCEPCorreios, consultar_cep, '37503130')

    def test_formatar_cep(self):
        self.assertRaises(ValueError, formatar_cep, 37503003)
        self.assertRaises(ValueError, formatar_cep, '')
        self.assertRaises(ValueError, formatar_cep, None)
        self.assertRaises(ValueError, formatar_cep, False)
        self.assertRaises(ValueError, formatar_cep, True)
        self.assertEqual(formatar_cep('37.503-003'), '37503003')
        self.assertEqual(formatar_cep('   37.503-003'), '37503003')
        self.assertEqual(formatar_cep('37 503-003'), '37503003')
        self.assertEqual(formatar_cep('37.503&003saasd'), '37503003')
        self.assertEqual(formatar_cep('\n \r 37.503-003'), '37503003')
        self.assertEqual(formatar_cep('\n \r 37.503-003'), '37503003')
        # ponto e virgula
        self.assertEqual(formatar_cep('37.503-003;'), '37503003')
        # Unicode Greek Question Mark
        self.assertEqual(formatar_cep(u'37.503-003;'), '37503003')

    def test_validar_cep(self):
        self.assertRaises(ValueError, validar_cep, 37503003)
        self.assertRaises(ValueError, validar_cep, '')
        self.assertIs(validar_cep('37.503-003'), True)
        self.assertIs(validar_cep('37.503-00'), False)
        self.assertIs(validar_cep('   37.503-003'), True)
        self.assertIs(validar_cep('37.503&003saasd'), True)

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
        msg = 'BUSCA DEFINIDA COMO EXATA, 0 CEP DEVE TER 8 DIGITOS'
        self.assertEqual(fault.strip(), msg)
