import pytest


from brazilcep import WebService, exceptions, get_address_from_cep


def test_fetch_address_success_real():
    address = get_address_from_cep("37.503-130", webservice=WebService.CORREIOS)
    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == "até 214/215"
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"


def test_fetch_address_fail_real():
    with pytest.raises(exceptions.InvalidCEP):
        get_address_from_cep("99999-999", webservice=WebService.CORREIOS)
