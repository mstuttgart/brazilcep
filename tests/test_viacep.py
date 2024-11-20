import logging
import os

import pytest
import requests
from dotenv import load_dotenv

from brazilcep import WebService, exceptions, get_address_from_cep

logger = logging.getLogger(__name__)

load_dotenv()
IN_GITHUB_ACTIONS = os.getenv("GITHUB_ACTIONS") == "true"
SKIP_REAL_TEST = os.getenv("SKIP_REAL_TEST", False)


@pytest.mark.skipif(SKIP_REAL_TEST, reason="Skip real teste API.")
@pytest.mark.skipif(IN_GITHUB_ACTIONS, reason="Test doesn't work in Github Actions.")
def test_get_address_from_cep_success_real():
    try:
        address = get_address_from_cep("37.503-130", webservice=WebService.VIACEP)

        assert address["district"] == "Santo Antônio"
        assert address["cep"] == "37503-130"
        assert address["city"] == "Itajubá"
        assert address["complement"] == "até 214/215"
        assert address["street"] == "Rua Geraldino Campista"
        assert address["uf"] == "MG"

    except requests.exceptions.ConnectionError as exc:
        logger.warning(exc)


def test_get_address_from_cep_success(requests_mock):
    """Set mock get return"""
    req_mock_text = """{
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

    requests_mock.get("http://www.viacep.com.br/ws/37503130/json", text=req_mock_text)

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
