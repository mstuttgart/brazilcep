from unittest import TestCase, mock

import pytest

from pycep_correios import consultar_cep, excecoes, formatar_cep, validar_cep


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

        assert endereco['bairro'] == 'Santo Antônio'
        assert endereco['cep'] == '37503130'
        assert endereco['cidade'] == 'Itajubá'
        assert endereco['complemento2'] == '- até 214/215'
        assert endereco['end'] == 'Rua Geraldino Campista'
        assert endereco['uf'] == 'MG'
        assert endereco['unidadesPostagem'] == []

        # Verifica se o metodo consultaCEP foi chamado
        # com os parametros corretos
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

        assert endereco['bairro'] == ''
        assert endereco['cep'] == ''
        assert endereco['cidade'] == ''
        assert endereco['complemento2'] == ''
        assert endereco['end'] == ''
        assert endereco['uf'] == ''
        assert endereco['unidadesPostagem'] == []

    def test_formatar_cep(self):

        with pytest.raises(ValueError):
            formatar_cep(37503003)

        with pytest.raises(ValueError):
            formatar_cep('')

        with pytest.raises(ValueError):
            formatar_cep(None)

        with pytest.raises(ValueError):
            formatar_cep(False)

        with pytest.raises(ValueError):
            formatar_cep(True)

        assert formatar_cep('37.503-003') == '37503003'
        assert formatar_cep('   37.503-003') == '37503003'
        assert formatar_cep('37 503-003') == '37503003'
        assert formatar_cep('37.503&003saasd') == '37503003'
        assert formatar_cep('\n \r 37.503-003') == '37503003'
        assert formatar_cep('\n \r 37.503-003') == '37503003'

        # ponto e virgula
        self.assertEqual(formatar_cep('37.503-003;'), '37503003')

        # Unicode Greek Question Mark
        self.assertEqual(formatar_cep(u'37.503-003;'), '37503003')

    def test_validar_cep(self):

        with pytest.raises(ValueError):
            validar_cep(37503003)

        with pytest.raises(ValueError):
            validar_cep('')

        assert validar_cep('37.503-003')
        assert validar_cep('   37.503-003')
        assert validar_cep('37.503&003saasd')

        assert not validar_cep('37.503-00')

    def test_consultar_cep_integration(self):

        # Aqui realizamos um teste de integração
        # pra garantir o funcionamento do todo

        # Realizamos a consulta de CEP
        try:
            endereco = consultar_cep('37.503-130')
        except excecoes.ExcecaoPyCEPCorreios as exc:
            print(exc.message)

        assert endereco['bairro'] == 'Santo Antônio'
        assert endereco['cep'] == '37503130'
        assert endereco['cidade'] == 'Itajubá'
        assert endereco['complemento2'] == '- até 214/215'
        assert endereco['end'] == 'Rua Geraldino Campista'
        assert endereco['uf'] == 'MG'
        assert endereco['unidadesPostagem'] == []
