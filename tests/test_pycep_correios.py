from unittest import TestCase, mock

from pycep_correios import consultar_cep, formatar_cep, validar_cep
from pycep_correios import excecoes


class TestPyCEPCorreios(TestCase):

    def setUp(self):
        self.expected_address = {
            'bairro': 'Santo Antônio',
            'cep': '37503130',
            'cidade': 'Itajubá',
            'end': 'Rua Geraldino Campista',
            'uf': 'MG',
            'complemento2': '- até 214/215',
            'unidadesPostagem': [],
        }

    @mock.patch('zeep.Client')
    def test_consultar_cep(self, mk):

        class MockClass:
            def __init__(self, dictionary):
                for k, v in dictionary.items():
                    setattr(self, k, v)

        end_esperado = {
            'bairro': 'Santo Antônio',
            'cep': '37503130',
            'cidade': 'Itajubá',
            'complemento2': '- até 214/215',
            'end': 'Rua Geraldino Campista',
            'uf': 'MG',
            'unidadesPostagem': [],
        }

        service_mk = mk.return_value.service

        # Criamos o mock para o valor de retorno
        service_mk.consultaCEP.return_value = MockClass(end_esperado)

        # Realizamos a consulta de CEP
        endereco = consultar_cep('37.503-130')

        self.assertEqual(endereco['bairro'], 'Santo Antônio')
        self.assertEqual(endereco['cep'], '37503130')
        self.assertEqual(endereco['cidade'], 'Itajubá')
        self.assertEqual(endereco['complemento2'], '- até 214/215')
        self.assertEqual(endereco['end'], 'Rua Geraldino Campista')
        self.assertEqual(endereco['uf'], 'MG')
        self.assertEqual(endereco['unidadesPostagem'], [])

        # Verifica se o metodo consultaCEP foi chamado com os parametros corretos
        service_mk.consultaCEP.assert_called_with('37503130')


    @mock.patch('zeep.Client')
    def test_consultar_return_error(self, mk):

        class MockClass:
            def __init__(self, dictionary):
                for k, v in dictionary.items():
                    setattr(self, k, v)

        # Utilizamps um retorno vazio para testar o retorno
        # com atributos ausentes
        end_esperado = {
        }

        service_mk = mk.return_value.service

        # Criamos o mock para o valor de retorno
        service_mk.consultaCEP.return_value = MockClass(end_esperado)

        # Realizamos a consulta de CEP
        endereco = consultar_cep('37.503-130')

        self.assertEqual(endereco['bairro'], '')
        self.assertEqual(endereco['cep'], '')
        self.assertEqual(endereco['cidade'], '')
        self.assertEqual(endereco['complemento2'], '')
        self.assertEqual(endereco['end'], '')
        self.assertEqual(endereco['uf'], '')
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

    def test_consultar_cep_integration(self):

        # Aqui realizamos um teste de integração
        # pra garantir o funcionamento do todo

        # Realizamos a consulta de CEP
        try:
            endereco = consultar_cep('37.503-130')
        except excecoes.ExcecaoPyCEPCorreios as exc:
            print(exc.message)

        self.assertEqual(endereco['bairro'], 'Santo Antônio')
        self.assertEqual(endereco['cep'], '37503130')
        self.assertEqual(endereco['cidade'], 'Itajubá')
        self.assertEqual(endereco['complemento2'], '- até 214/215')
        self.assertEqual(endereco['end'], 'Rua Geraldino Campista')
        self.assertEqual(endereco['uf'], 'MG')
        self.assertEqual(endereco['unidadesPostagem'], [])

