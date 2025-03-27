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

# Constants
IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"
SKIP_REAL_TEST = os.getenv("SKIP_REAL_TEST", True)
BASE_URL = "https://opencep.com/v1/"

RESPONSE_MOCK_TEXT_SUCCESS = """{
    "cep": "37503-130",
    "logradouro": "Rua Geraldino Campista",
    "complemento": "até 214/215",
    "bairro": "Santo Antônio",
    "localidade": "Itajubá",
    "uf": "MG",
    "ibge": "3132404"
}"""


@pytest.mark.skipif(
    SKIP_REAL_TEST or IN_GITHUB_ACTIONS, reason="Skip real API tests in certain environments."
)
def test_fetch_address_success_real():
    """
    Test fetching a valid address from the real API.
    """
    address = get_address_from_cep("37.503-130", webservice=WebService.OPENCEP)

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
    Test fetching an invalid CEP from the real API.
    """
    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep("00000-000", webservice=WebService.OPENCEP)


def test_fetch_address_success(requests_mock):
    """
    Test fetching a valid address using mocked requests.
    """
    requests_mock.get(f"{BASE_URL}37503130", text=RESPONSE_MOCK_TEXT_SUCCESS, status_code=200)

    address = get_address_from_cep("37.503-130", webservice=WebService.OPENCEP, timeout=5)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
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

    requests_mock.get(f"{BASE_URL}99999999", text=req_mock_text, status_code=200)

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
    """
    Test fetching an invalid CEP using mocked requests.
    """
    requests_mock.get(f"{BASE_URL}00000000", status_code=404)

    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep("00000-000", webservice=WebService.OPENCEP)


def test_fetch_address_500(requests_mock):
    """
    Test handling a 500 Internal Server Error response.
    """
    requests_mock.get(f"{BASE_URL}37503130", status_code=500)

    with pytest.raises(exceptions.BrazilCEPException):
        get_address_from_cep("37503-130", webservice=WebService.OPENCEP)


def test_json_decode_error(requests_mock):
    """Test json decode error."""

    requests_mock.get(f"{BASE_URL}37503130", text=RESPONSE_MOCK_TEXT_SUCCESS, status_code=200)

    with patch("brazilcep.opencep.json.loads", side_effect=json.JSONDecodeError("", "", 0)):
        with pytest.raises(exceptions.BrazilCEPException):
            get_address_from_cep("37503-130", webservice=WebService.OPENCEP)


@pytest.mark.skipif(
    SKIP_REAL_TEST or IN_GITHUB_ACTIONS, reason="Skip real API tests in certain environments."
)
@pytest.mark.asyncio
async def test_async_fetch_address_success_real():
    """
    Test fetching an address asynchronously using real API.
    """
    address = await async_get_address_from_cep("37503-130", webservice=WebService.OPENCEP)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == ""
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"


@pytest.mark.asyncio
async def test_async_get_address_from_cep_success():
    """
    Test fetching an address asynchronously using mocked aiohttp.
    """

    async def __mock_aiohttp_get(*args, **kwargs):
        return 200, RESPONSE_MOCK_TEXT_SUCCESS

    with patch("brazilcep.opencep.utils.aiohttp_get", side_effect=__mock_aiohttp_get):
        result = await async_get_address_from_cep("37503-130", webservice=WebService.OPENCEP)
        assert isinstance(result, dict)
