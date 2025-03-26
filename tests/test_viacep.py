import logging
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

logger = logging.getLogger(__name__)

dotenv.load_dotenv()

IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"
SKIP_REAL_TEST = os.getenv("SKIP_REAL_TEST", False)

RESPONSE_MOCK_TEXT_SUCCESS = """{
    \n  "cep": "37503-130",
    \n  "logradouro": "Rua Geraldino Campista",
    \n  "complemento": "até 214/215",
    \n  "bairro": "Santo Antônio",
    \n  "localidade": "Itajubá",
    \n  "uf": "MG",
    \n  "ibge": "3132404",
    \n  "gia": "",
    \n  "ddd": "35",
    \n  "siafi": "4647"
\n}"""


@pytest.mark.skipif(SKIP_REAL_TEST, reason="Skip real teste API.")
@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_get_address_from_cep_success_real():
    address = get_address_from_cep("37.503-130", webservice=WebService.VIACEP)

    assert address["district"] == "Santo Antônio"
    assert address["cep"] == "37503-130"
    assert address["city"] == "Itajubá"
    assert address["complement"] == "até 214/215"
    assert address["street"] == "Rua Geraldino Campista"
    assert address["uf"] == "MG"


@pytest.mark.skipif(SKIP_REAL_TEST, reason="Skip real teste API.")
@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_get_address_from_cep_not_found_real():
    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep("00000-000", webservice=WebService.VIACEP)


def test_get_address_from_cep_success(requests_mock):
    """Set mock get return"""
    requests_mock.get("http://www.viacep.com.br/ws/37503130/json", text=RESPONSE_MOCK_TEXT_SUCCESS)

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
    req_mock_text = """{
        \n  "erro": "true"\n
    }"""

    requests_mock.get("http://www.viacep.com.br/ws/00000000/json", text=req_mock_text)

    # Realizamos a consulta de CEP
    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep("00000-000", webservice=WebService.VIACEP)

    requests_mock.get("http://www.viacep.com.br/ws/99999999/json", text=req_mock_text)

    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep("99999-999", webservice=WebService.VIACEP)


def test_get_address_invalid_cep(requests_mock):
    requests_mock.get("http://www.viacep.com.br/ws/3750313/json", status_code=400)

    with pytest.raises(exceptions.InvalidCEP):
        get_address_from_cep("37503-13", webservice=WebService.VIACEP)


def test_fetch_address_404(requests_mock):
    requests_mock.get("http://www.viacep.com.br/ws/37503130/json", status_code=404)  # noqa

    with pytest.raises(exceptions.BrazilCEPException):
        get_address_from_cep("37503-130", webservice=WebService.VIACEP)


def test_connection_error(requests_mock):
    requests_mock.get(
        "http://www.viacep.com.br/ws/37503130/json", exc=requests.exceptions.ConnectionError
    )

    with pytest.raises(exceptions.ConnectionError):
        get_address_from_cep("37503-130", webservice=WebService.VIACEP)


def test_http_error(requests_mock):
    requests_mock.get(
        "http://www.viacep.com.br/ws/37503130/json", exc=requests.exceptions.HTTPError
    )

    with pytest.raises(exceptions.HTTPError):
        get_address_from_cep("37503-130", webservice=WebService.VIACEP)


def test_url_required_error(requests_mock):
    requests_mock.get(
        "http://www.viacep.com.br/ws/37503130/json", exc=requests.exceptions.URLRequired
    )

    with pytest.raises(exceptions.URLRequired):
        get_address_from_cep("37503-130", webservice=WebService.VIACEP)


def test_too_many_redirects_error(requests_mock):
    requests_mock.get(
        "http://www.viacep.com.br/ws/37503130/json", exc=requests.exceptions.TooManyRedirects
    )

    with pytest.raises(exceptions.TooManyRedirects):
        get_address_from_cep("37503-130", webservice=WebService.VIACEP)


def test_timeout_error(requests_mock):
    requests_mock.get("http://www.viacep.com.br/ws/37503130/json", exc=requests.exceptions.Timeout)

    with pytest.raises(exceptions.Timeout):
        get_address_from_cep("37503-130", webservice=WebService.VIACEP)


@pytest.mark.asyncio
async def test_async_get_address_from_cep():
    async def __mock_aiohttp_get(*args, **kwargs):
        return 200, RESPONSE_MOCK_TEXT_SUCCESS

    with patch("brazilcep.opencep.aiohttp_get", side_effect=__mock_aiohttp_get):
        result = await async_get_address_from_cep("37503-130", webservice=WebService.VIACEP)
        assert isinstance(result, dict)
