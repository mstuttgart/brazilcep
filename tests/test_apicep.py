import os
from unittest.mock import patch

import dotenv
import pytest
import requests

from brazilcep import (
    WebService,
    async_get_address_from_cep,
    exceptions,
    get_address_from_cep,
)

dotenv.load_dotenv()

IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"
SKIP_REAL_TEST = os.getenv("SKIP_REAL_TEST", True)

RESPONSE_MOCK_TEXT_SUCCESS = """{
    "status":200,
    "ok":true,
    "code":"37503-130",
    "state":"MG",
    "city":"Itajubá",
    "district":"Santo Antônio",
    "address":"Rua Geraldino Campista - até 214/215",
    "statusText":"ok"
}"""


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


@pytest.mark.skipif(SKIP_REAL_TEST, reason="Skip real teste API.")
@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_fetch_address_cep_not_found_real():
    with pytest.raises(exceptions.InvalidCEP):
        get_address_from_cep("37.503-13", webservice=WebService.APICEP)


def test_fetch_address_success(requests_mock):
    requests_mock.get("https://ws.apicep.com/cep/37503130.json", text=RESPONSE_MOCK_TEXT_SUCCESS)

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
    req_mock_text_400 = """{
        "status":400,
        "message": "Blocked by flood"
    }"""

    requests_mock.get("https://ws.apicep.com/cep/37503130.json", text=req_mock_text_400)

    with pytest.raises(exceptions.BlockedByFlood):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


def test_fetch_address_429(requests_mock):
    requests_mock.get("https://ws.apicep.com/cep/37503130.json", status_code=429)

    with pytest.raises(exceptions.BlockedByFlood):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


def test_fetch_address_404(requests_mock):
    requests_mock.get("https://ws.apicep.com/cep/37503130.json", status_code=404)

    with pytest.raises(exceptions.BrazilCEPException):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


def test_connection_error(requests_mock):
    requests_mock.get(
        "https://ws.apicep.com/cep/37503130.json", exc=requests.exceptions.ConnectionError
    )

    with pytest.raises(exceptions.ConnectionError):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


def test_http_error(requests_mock):
    requests_mock.get("https://ws.apicep.com/cep/37503130.json", exc=requests.exceptions.HTTPError)

    with pytest.raises(exceptions.HTTPError):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


def test_url_required_error(requests_mock):
    requests_mock.get(
        "https://ws.apicep.com/cep/37503130.json", exc=requests.exceptions.URLRequired
    )

    with pytest.raises(exceptions.URLRequired):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


def test_too_many_redirects_error(requests_mock):
    requests_mock.get(
        "https://ws.apicep.com/cep/37503130.json", exc=requests.exceptions.TooManyRedirects
    )

    with pytest.raises(exceptions.TooManyRedirects):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


def test_timeout_error(requests_mock):
    requests_mock.get("https://ws.apicep.com/cep/37503130.json", exc=requests.exceptions.Timeout)

    with pytest.raises(exceptions.Timeout):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


@pytest.mark.asyncio
async def test_async_get_address_from_cep():
    async def __mock_aiohttp_get(*args, **kwargs):
        return 200, RESPONSE_MOCK_TEXT_SUCCESS

    with patch("brazilcep.apicep.aiohttp_get", side_effect=__mock_aiohttp_get):
        result = await async_get_address_from_cep("37503-130", webservice=WebService.APICEP)
        assert isinstance(result, dict)
