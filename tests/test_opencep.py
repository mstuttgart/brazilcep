import os

import pytest
from dotenv import load_dotenv

from brazilcep import WebService, exceptions, get_address_from_cep

load_dotenv()
IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"
SKIP_REAL_TEST = os.getenv("SKIP_REAL_TEST", True)


@pytest.mark.skipif(SKIP_REAL_TEST, reason="Skip real teste API.")
@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_fetch_address_success_real():
    address = get_address_from_cep("37.503-130", webservice=WebService.OPENCEP)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == ""
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"


def test_fetch_address_success(requests_mock):
    req_mock_text = """{
        "cep": "37503-130",
        "logradouro": "Rua Geraldino Campista",
        "complemento": "até 214/215",
        "bairro": "Santo Antônio",
        "localidade": "Itajubá",
        "uf": "MG",
        "ibge": "3132404"
    }"""

    requests_mock.get("https://opencep.com/v1/37503130", text=req_mock_text, status_code=200)

    address = get_address_from_cep("37.503-130", webservice=WebService.OPENCEP, timeout=5)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == ""
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"

    req_mock_text = """{
        "cep": "99999-999",
        "logradouro": "Avenida das Torres",
        "complemento": "até 99999999 - lado ímpar",
        "unidade": "",
        "bairro": "Jardim Centro Cívico",
        "localidade": "Sarandi",
        "uf": "PR",
        "ibge": "4126256"
    }"""

    requests_mock.get("https://opencep.com/v1/99999999", text=req_mock_text, status_code=200)

    proxies = {"https": "00.00.000.000", "http": "00.00.000.000"}

    address = get_address_from_cep(
        "99999-999", webservice=WebService.OPENCEP, timeout=6, proxies=proxies
    )

    assert address["district"] == "Jardim Centro Cívico"
    assert address["cep"] == "99999-999"
    assert address["city"] == "Sarandi"
    assert address["complement"] == ""
    assert address["street"] == "Avenida das Torres"
    assert address["uf"] == "PR"


def test_fetch_address_cep_not_found(requests_mock):
    requests_mock.get("https://opencep.com/v1/00000000", status_code=404)

    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep("00000-000", webservice=WebService.OPENCEP)


def test_fetch_address_500(requests_mock):
    requests_mock.get("https://opencep.com/v1/37503130", status_code=500)

    with pytest.raises(exceptions.BrazilCEPException):
        get_address_from_cep("37503-130", webservice=WebService.OPENCEP)
