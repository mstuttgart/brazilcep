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
SKIP_REAL_TEST = os.getenv("SKIP_REAL_TEST", False)

BASE_URL = "http://www.viacep.com.br/ws"
RESPONSE_MOCK_TEXT_SUCCESS = """{
    "cep": "37503-130",
    "logradouro": "Rua Geraldino Campista",
    "complemento": "até 214/215",
    "bairro": "Santo Antônio",
    "localidade": "Itajubá",
    "uf": "MG",
    "ibge": "3132404",
    "gia": "",
    "ddd": "35",
    "siafi": "4647"
}"""


@pytest.mark.skipif(
    SKIP_REAL_TEST or IN_GITHUB_ACTIONS,
    reason="Skip real API tests in certain environments.",
)
def test_get_address_from_cep_success_real():
    """
    Test successful address retrieval from real API.
    """
    address = get_address_from_cep("37.503-130", webservice=WebService.VIACEP)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == "até 214/215"
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"


@pytest.mark.skipif(
    SKIP_REAL_TEST or IN_GITHUB_ACTIONS,
    reason="Skip real API tests in certain environments.",
)
def test_get_address_from_cep_not_found_real():
    """
    Test address not found scenario with real API.
    """
    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep("00000-000", webservice=WebService.VIACEP)


def test_get_address_from_cep_success(requests_mock):
    """
    Test successful address retrieval with mocked API.
    """
    requests_mock.get(f"{BASE_URL}/37503130/json", text=RESPONSE_MOCK_TEXT_SUCCESS)

    proxies = {"https": "00.00.000.000", "http": "00.00.000.000"}

    address = get_address_from_cep(
        "37.503-130", webservice=WebService.VIACEP, timeout=10, proxies=proxies
    )

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == "até 214/215"
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"


def test_get_address_from_cep_not_found(requests_mock):
    """
    Test address not found scenario with mocked API.
    """
    mock_response = '{"erro": "true"}'

    requests_mock.get(f"{BASE_URL}/00000000/json", text=mock_response)
    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep("00000-000", webservice=WebService.VIACEP)

    requests_mock.get(f"{BASE_URL}/99999999/json", text=mock_response)
    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep("99999-999", webservice=WebService.VIACEP)


def test_get_address_invalid_cep(requests_mock):
    """
    Test invalid CEP scenario.
    """
    requests_mock.get(f"{BASE_URL}/3750313/json", status_code=400)

    with pytest.raises(exceptions.InvalidCEP):
        get_address_from_cep("37503-13", webservice=WebService.VIACEP)


def test_fetch_address_404(requests_mock):
    """
    Test 404 error scenario.
    """
    requests_mock.get(f"{BASE_URL}/37503130/json", status_code=404)

    with pytest.raises(exceptions.BrazilCEPException):
        get_address_from_cep("37503-130", webservice=WebService.VIACEP)


def test_json_decode_error(requests_mock):
    """
    Test json decode error.
    """

    requests_mock.get(f"{BASE_URL}/37503130/json", text=RESPONSE_MOCK_TEXT_SUCCESS)

    with patch("brazilcep.viacep.json.loads", side_effect=json.JSONDecodeError("", "", 0)):
        with pytest.raises(exceptions.BrazilCEPException):
            get_address_from_cep("37503-130", webservice=WebService.VIACEP)


@pytest.mark.skipif(
    SKIP_REAL_TEST or IN_GITHUB_ACTIONS, reason="Skip real API tests in certain environments."
)
@pytest.mark.asyncio
async def test_async_fetch_address_success_real():
    """
    Test fetching an address asynchronously using real API.
    """
    address = await async_get_address_from_cep("37503-130", webservice=WebService.VIACEP)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == "até 214/215"
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"


@pytest.mark.asyncio
async def test_async_get_address_from_cep_success():
    """
    Test asynchronous address retrieval.
    """

    async def __mock_aiohttp_get(*args, **kwargs):
        return 200, RESPONSE_MOCK_TEXT_SUCCESS

    with patch("brazilcep.opencep.utils.aiohttp_get", side_effect=__mock_aiohttp_get):
        result = await async_get_address_from_cep("37503-130", webservice=WebService.VIACEP)
        assert isinstance(result, dict)
