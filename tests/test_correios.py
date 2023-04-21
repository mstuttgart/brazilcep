from unittest import mock

import pytest
import zeep

from brazilcep import WebService, exceptions, get_address_from_cep


@mock.patch("zeep.Client")
def test_fetch_address_success(mk):
    class MockClass:
        def __init__(self, dictionary):
            for k, v in dictionary.items():
                setattr(self, k, v)

    expected_address = {
        "bairro": "Santo Antônio",
        "cep": "37503130",
        "cidade": "Itajubá",
        "complemento2": "- até 214/215",
        "end": "Rua Geraldino Campista",
        "uf": "MG",
        "unidadesPostagem": [],
    }

    service_mk = mk.return_value.service

    # Criamos o mock para o valor de retorno
    service_mk.consultaCEP.return_value = MockClass(expected_address)

    # Realizamos a consulta de CEP
    address = get_address_from_cep("37503130", webservice=WebService.CORREIOS)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == "- até 214/215"
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"

    # Verifica se o metodo consultaCEP foi chamado
    # com os parametros corretos
    service_mk.consultaCEP.assert_called_with("37503130")


@mock.patch("zeep.Client")
def test_fetch_address_success_unique(mk):
    class MockClass:
        def __init__(self, dictionary):
            for k, v in dictionary.items():
                setattr(self, k, v)

    expected_address = {
        "bairro": "",
        "cep": "9999999",
        "cidade": "Sarandi",
        "complemento2": "",
        "end": "",
        "uf": "PR",
        "unidadesPostagem": [],
    }

    service_mk = mk.return_value.service

    # Criamos o mock para o valor de retorno
    service_mk.consultaCEP.return_value = MockClass(expected_address)

    # Realizamos a consulta de CEP
    address = get_address_from_cep("37503130", webservice=WebService.CORREIOS)

    assert address["district"] == ""
    assert address["cep"] == "9999999"
    assert address["city"] == "Sarandi"
    assert address["complement"] == ""
    assert address["street"] == ""
    assert address["uf"] == "PR"

    # Verifica se o metodo consultaCEP foi chamado
    # com os parametros corretos
    service_mk.consultaCEP.assert_called_with("37503130")


@mock.patch("zeep.Client")
def test_fetch_address_fail(mk):
    class MockClass:
        def __init__(self, dictionary):
            for k, v in dictionary.items():
                setattr(self, k, v)

    service_mk = mk.return_value.service

    # Criamos o mock para o valor de retorno
    service_mk.consultaCEP.side_effect = zeep.exceptions.Fault("error", 500)

    with pytest.raises(exceptions.BrazilCEPException):
        get_address_from_cep("37503130", webservice=WebService.CORREIOS)
