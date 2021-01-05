
import pytest

from pycep_correios import WebService, exceptions, get_address_from_cep


def test_fetch_address_success():

    # Realizamos a consulta de CEP
    address = get_address_from_cep('37.503-130', webservice=WebService.APICEP)

    assert address['bairro'] == 'Santo Antônio'
    assert address['cep'] == '37503-130'
    assert address['cidade'] == 'Itajubá'
    assert address['complemento'] == ''
    assert address['logradouro'] == 'Rua Geraldino Campista'
    assert address['uf'] == 'MG'


def test_fetch_address_fail():

    # Realizamos a consulta de CEP
    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep('00000-000', webservice=WebService.APICEP)

    with pytest.raises(exceptions.InvalidCEP):
        get_address_from_cep('37503-13', webservice=WebService.APICEP)
