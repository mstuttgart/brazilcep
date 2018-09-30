# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import unittest

from pycep_correios import consultar_cep, formatar_cep, validar_cep
from pycep_correios import HOMOLOGACAO, PRODUCAO


class TestPyCEPCorreios(unittest.TestCase):

    def setUp(self):
        self.expected_address = {
            'bairro': 'Santo Antônio',
            'cep': '37503130',
            'cidade': 'Itajubá',
            'end': 'Rua Geraldino Campista',
            'id': 0,
            'uf': 'MG',
            'complemento': '',
            'complemento2': '- até 214/215',
        }

    def test_consultar_cep(self):

        # Realizamos a consulta de CEP
        endereco = consultar_cep('37.503-130')

        self.assertEqual(endereco.bairro, 'Santo Antônio')
        self.assertEqual(endereco.cep, '37503130')
        self.assertEqual(endereco.cidade, 'Itajubá')
        self.assertEqual(endereco.complemento, None)
        self.assertEqual(endereco.complemento2, '- até 214/215')
        self.assertEqual(endereco.end, 'Rua Geraldino Campista')
        self.assertEqual(endereco.id, 0)
        self.assertEqual(endereco.uf, 'MG')
        self.assertEqual(endereco.unidadesPostagem, [])

        endereco = consultar_cep('37503130')

        self.assertEqual(endereco['bairro'], 'Santo Antônio')
        self.assertEqual(endereco['cep'], '37503130')
        self.assertEqual(endereco['cidade'], 'Itajubá')
        self.assertEqual(endereco['complemento'], None)
        self.assertEqual(endereco['complemento2'], '- até 214/215')
        self.assertEqual(endereco['end'], 'Rua Geraldino Campista')
        self.assertEqual(endereco['id'], 0)
        self.assertEqual(endereco['uf'], 'MG')
        self.assertEqual(endereco['unidadesPostagem'], [])

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
