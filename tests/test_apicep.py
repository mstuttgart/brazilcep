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
    address = get_address_from_cep("37.503-130", webservice=WebService.APICEP)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == ""
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"


def test_fetch_address_success(requests_mock):
    req_mock_text = """{
        "status":200,
        "ok":true,
        "code":"37503-130",
        "state":"MG",
        "city":"Itajubá",
        "district":"Santo Antônio",
        "address":"Rua Geraldino Campista - até 214/215",
        "statusText":"ok"
    }"""

    requests_mock.get("https://ws.apicep.com/cep/37503130.json", text=req_mock_text)

    address = get_address_from_cep("37.503-130", webservice=WebService.APICEP, timeout=5)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == ""
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"

    req_mock_text = """{
        "status":200,
        "ok":true,
        "code":"99999-999",
        "state":"PR",
        "city":"Sarandi",
        "district":null,
        "address":null,
        "statusText":"ok"
    }"""

    requests_mock.get("https://ws.apicep.com/cep/99999999.json", text=req_mock_text)

    proxies = {"https": "00.00.000.000", "http": "00.00.000.000"}

    address = get_address_from_cep(
        "99999-999", webservice=WebService.APICEP, timeout=5, proxies=proxies
    )

    assert address["district"] == ""
    assert address["cep"] == "99999-999"
    assert address["city"] == "Sarandi"
    assert address["complement"] == ""
    assert address["street"] == ""
    assert address["uf"] == "PR"


def test_fetch_address_cep_not_found(requests_mock):
    req_mock_text = """{
        "status":404
    }"""

    requests_mock.get("https://ws.apicep.com/cep/00000000.json", text=req_mock_text)

    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep("00000-000", webservice=WebService.APICEP)


def test_fetch_address_invalid_cep(requests_mock):
    req_mock_text = """{
        "status":400,
        "message": "CEP informado é inválido"
    }"""

    requests_mock.get("https://ws.apicep.com/cep/3750313.json", text=req_mock_text)

    with pytest.raises(exceptions.InvalidCEP):
        get_address_from_cep("37503-13", webservice=WebService.APICEP)


def test_fetch_address_blocked_by_flood(requests_mock):
    req_mock_text = """{
        "status":400,
        "message": "Blocked by flood"
    }"""

    requests_mock.get("https://ws.apicep.com/cep/3750313.json", text=req_mock_text)

    with pytest.raises(exceptions.BlockedByFlood):
        get_address_from_cep("37503-13", webservice=WebService.APICEP)


def test_fetch_address_404(requests_mock):
    requests_mock.get("https://ws.apicep.com/cep/37503130.json", status_code=404)

    with pytest.raises(exceptions.BrazilCEPException):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)
