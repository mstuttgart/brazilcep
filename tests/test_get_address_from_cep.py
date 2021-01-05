
from unittest import mock

import pytest

from pycep_correios import get_address_from_cep, WebService


def test_search_error():

    with pytest.raises(KeyError):
        get_address_from_cep('37.503-130', webservice=5)

    with pytest.raises(KeyError):
        get_address_from_cep('37.503-130', webservice='VIACEP')

    with pytest.raises(ValueError):
        get_address_from_cep('37.503-13')

    with pytest.raises(ValueError):
        get_address_from_cep(3750313)


def test_viacep_success():

    # Realizamos a consulta de CEP
    endereco = get_address_from_cep('37.503-130', webservice=WebService.VIACEP)

    assert endereco['bairro'] == 'Santo Antônio'
    assert endereco['cep'] == '37503-130'
    assert endereco['cidade'] == 'Itajubá'
    assert endereco['complemento'] == 'até 214/215'
    assert endereco['logradouro'] == 'Rua Geraldino Campista'
    assert endereco['uf'] == 'MG'


def test_apicep_success():

    # Realizamos a consulta de CEP
    endereco = get_address_from_cep('37.503-130', webservice=WebService.APICEP)

    assert endereco['bairro'] == 'Santo Antônio'
    assert endereco['cep'] == '37503-130'
    assert endereco['cidade'] == 'Itajubá'
    assert endereco['complemento'] == ''
    assert endereco['logradouro'] == 'Rua Geraldino Campista'
    assert endereco['uf'] == 'MG'


@mock.patch('zeep.Client')
def test_apicorreios_success(mk):
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
    endereco = get_address_from_cep('37.503-130', webservice=WebService.CORREIOS)

    assert endereco['bairro'] == 'Santo Antônio'
    assert endereco['cep'] == '37503130'
    assert endereco['cidade'] == 'Itajubá'
    assert endereco['complemento'] == '- até 214/215'
    assert endereco['logradouro'] == 'Rua Geraldino Campista'
    assert endereco['uf'] == 'MG'

    # Verifica se o metodo consultaCEP foi chamado
    # com os parametros corretos
    service_mk.consultaCEP.assert_called_with('37503130')
