import json
import os
from unittest.mock import patch

import dotenv
import pytest

from brazilcep import (
    WebService,
    async_get_address_from_cep,
    exceptions,
    get_address_from_cep,
)

dotenv.load_dotenv()

IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"
SKIP_REAL_TEST = os.getenv("SKIP_REAL_TEST", True)

# Constants for mock responses
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

API_URL = "https://ws.apicep.com/cep"


@pytest.mark.skipif(
    SKIP_REAL_TEST or IN_GITHUB_ACTIONS, reason="Skip real API tests in certain environments."
)
def test_fetch_address_success_real():
    """
    Test successful address fetch with real API.
    """
    address = get_address_from_cep("37.503-130", webservice=WebService.APICEP)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == ""
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"


@pytest.mark.skipif(
    SKIP_REAL_TEST or IN_GITHUB_ACTIONS, reason="Skip real API tests in certain environments."
)
def test_fetch_address_cep_not_found_real():
    """
    Test invalid CEP with real API.
    """
    with pytest.raises(exceptions.InvalidCEP):
        get_address_from_cep("37.503-13", webservice=WebService.APICEP)


def test_fetch_address_success(requests_mock):
    """
    Test successful address fetch with mocked API.
    """

    requests_mock.get(f"{API_URL}/37503130.json", text=RESPONSE_MOCK_TEXT_SUCCESS)

    address = get_address_from_cep("37.503-130", webservice=WebService.APICEP, timeout=5)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == ""
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"

    # Test another mocked response
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

    requests_mock.get(f"{API_URL}/99999999.json", text=req_mock_text)

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
    """
    Test CEP not found error.
    """
    requests_mock.get(f"{API_URL}/00000000.json", text='{"status":404}')

    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep("00000-000", webservice=WebService.APICEP)


def test_fetch_address_invalid_cep(requests_mock):
    """
    Test invalid CEP error.
    """
    requests_mock.get(
        f"{API_URL}/3750313.json", text='{"status":400, "message": "CEP informado é inválido"}'
    )

    with pytest.raises(exceptions.InvalidCEP):
        get_address_from_cep("37503-13", webservice=WebService.APICEP)


def test_fetch_address_blocked_by_flood(requests_mock):
    """
    Test blocked by flood error.
    """
    requests_mock.get(
        f"{API_URL}/37503130.json", text='{"status":400, "message": "Blocked by flood"}'
    )

    with pytest.raises(exceptions.BlockedByFlood):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


def test_fetch_address_other_error_code_400(requests_mock):
    """
    Test status 400 code error.
    """
    requests_mock.get(f"{API_URL}/37503130.json", text='{"status":400, "message": "Unknown error"}')

    with pytest.raises(exceptions.BrazilCEPException):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


def test_fetch_address_429(requests_mock):
    """
    Test too many requests error.
    """
    requests_mock.get(f"{API_URL}/37503130.json", status_code=429)

    with pytest.raises(exceptions.BlockedByFlood):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


def test_fetch_address_404(requests_mock):
    """
    Test generic 404 error.
    """
    requests_mock.get(f"{API_URL}/37503130.json", status_code=404)

    with pytest.raises(exceptions.BrazilCEPException):
        get_address_from_cep("37503-130", webservice=WebService.APICEP)


def test_json_decode_error(requests_mock):
    """
    Test json decode error.
    """

    requests_mock.get(f"{API_URL}/37503130.json", text=RESPONSE_MOCK_TEXT_SUCCESS)

    with patch("brazilcep.apicep.json.loads", side_effect=json.JSONDecodeError("", "", 0)):
        with pytest.raises(exceptions.BrazilCEPException):
            get_address_from_cep("37503-130", webservice=WebService.APICEP)


@pytest.mark.skipif(
    SKIP_REAL_TEST or IN_GITHUB_ACTIONS, reason="Skip real API tests in certain environments."
)
@pytest.mark.asyncio
async def test_async_fetch_address_success_real():
    """
    Test fetching an address asynchronously using real API.
    """
    address = await async_get_address_from_cep("37503-130", webservice=WebService.APICEP)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == ""
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"


@pytest.mark.asyncio
async def test_async_get_address_from_cep_success():
    """
    Test async address fetch.
    """

    async def __mock_aiohttp_get(*args, **kwargs):
        return 200, RESPONSE_MOCK_TEXT_SUCCESS

    with patch("brazilcep.apicep.utils.aiohttp_get", side_effect=__mock_aiohttp_get):
        result = await async_get_address_from_cep("37503-130", webservice=WebService.APICEP)
        assert isinstance(result, dict)
