
from unittest import mock

from pycep_correios import WebService, get_address_from_cep


@mock.patch('zeep.Client')
def test_fetch_address_success(mk):
    class MockClass:
        def __init__(self, dictionary):
            for k, v in dictionary.items():
                setattr(self, k, v)

    expected_address = {
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
    service_mk.consultaCEP.return_value = MockClass(expected_address)

    # Realizamos a consulta de CEP
    endereco = get_address_from_cep('37503130', webservice=WebService.CORREIOS)

    assert endereco['bairro'] == 'Santo Antônio'
    assert endereco['cep'] == '37503130'
    assert endereco['cidade'] == 'Itajubá'
    assert endereco['complemento'] == '- até 214/215'
    assert endereco['logradouro'] == 'Rua Geraldino Campista'
    assert endereco['uf'] == 'MG'

    # Verifica se o metodo consultaCEP foi chamado
    # com os parametros corretos
    service_mk.consultaCEP.assert_called_with('37503130')
