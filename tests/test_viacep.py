
import pytest
from pycep_correios import (WebService, exceptions, get_address_from_cep,
                            get_cep_from_address)


def test_get_address_from_cep_success():

    # Realizamos a consulta de CEP
    address = get_address_from_cep('37.503-130', webservice=WebService.VIACEP)

    assert address['bairro'] == 'Santo Antônio'
    assert address['cep'] == '37503-130'
    assert address['cidade'] == 'Itajubá'
    assert address['complemento'] == 'até 214/215'
    assert address['logradouro'] == 'Rua Geraldino Campista'
    assert address['uf'] == 'MG'


def test_get_address_from_cep_fail():

    # Realizamos a consulta de CEP
    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep('00000-000', webservice=WebService.VIACEP)

    with pytest.raises(exceptions.InvalidCEP):
        get_address_from_cep('37503-13', webservice=WebService.VIACEP)


def test_fetch_cep_success():

    response = [
        {
            "cep": "37503-165",
            "logradouro": "Rua Geraldino Campista",
            "complemento": "de 871/872 ao fim",
            "bairro": "Santa Luzia",
            "localidade": "Itajubá",
            "uf": "MG",
            "ibge": "3132404",
            "gia": "",
            'ddd': '35',
            'siafi': '4647',
        },
        {
            "cep": "37503-130",
            "logradouro": "Rua Geraldino Campista",
            "complemento": "até 214/215",
            "bairro": "Santo Antônio",
            "localidade": "Itajubá",
            "uf": "MG",
            "ibge": "3132404",
            "gia": "",
            'ddd': '35',
            'siafi': '4647',
        },
        {
            "cep": "37503-003",
            "logradouro": "Rua Geraldino Campista",
            "complemento": "de 216/217 a 869/870",
            "bairro": "Vila Poddis",
            "localidade": "Itajubá",
            "uf": "MG",
            "ibge": "3132404",
            "gia": "",
            'ddd': '35',
            'siafi': '4647',
        }
    ]

    # Realizamos a consulta de enreço
    ceps = get_cep_from_address(
        state='MG', city='Itajuba', street='Rua Geraldino Campista')

    assert response == ceps


def test_fetch_cep_fail():

    # Realizamos a consulta de enreço
    ceps = get_cep_from_address(state='MG', city='Itaba', street='Rua Geraldino Campista')  # noqa

    assert ceps == []

    with pytest.raises(exceptions.InvalidCityStateName):
        get_cep_from_address(state='MG', city='It', street='Ru')  # noqa
