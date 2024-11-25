"""
brazilcep.viacep
~~~~~~~~~~~~~~~~

This module implements the BrazilCEP ViaCEP adapter.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

import json
from typing import Union

import requests

from . import exceptions

URL = "http://www.viacep.com.br/ws/{}/json"


def fetch_address(cep: str, timeout: Union[None, int], proxies: Union[None, dict]) -> dict:
    """Fetch APICEP webservice for CEP address. APICEP provide
    a REST API to query CEP requests.

    Args:
        cep: CEP to be searched
        timeout: How many seconds to wait for the server to return data before giving up
        proxies: Dictionary mapping protocol to the URL of the proxy

    Raises:
        exceptions.ConnectionError: raised by a connection error
        exceptions.HTTPError: raised by HTTP error
        exceptions.URLRequired: raised by using a invalid URL to make a request
        exceptions.TooManyRedirects: raised by too many redirects
        exceptions.Timeout: raised by request timed out
        exceptions.InvalidCEP: raised to invalid CEP requests
        exceptions.BlockedByFlood: raised by flood of requests
        exceptions.CEPNotFound: raised to CEP not founded requests
        exceptions.BrazilCEPException: Base class for exception

    Returns:
        Address data from CEP
    """

    try:
        response = requests.get(URL.format(cep), timeout=timeout, proxies=proxies)

    except requests.exceptions.ConnectionError as exc:
        raise exceptions.ConnectionError(exc)

    except requests.exceptions.HTTPError as exc:
        raise exceptions.HTTPError(exc)

    except requests.exceptions.URLRequired as exc:
        raise exceptions.URLRequired(exc)

    except requests.exceptions.TooManyRedirects as exc:
        raise exceptions.TooManyRedirects(exc)

    except requests.exceptions.Timeout as exc:
        raise exceptions.Timeout(exc)

    if response.status_code == 200:
        # Transforma o objeto requests em um dict
        address = json.loads(response.text)

        if address.get("erro"):
            raise exceptions.CEPNotFound()

        return {
            "district": address.get("bairro") or "",
            "cep": address.get("cep") or "",
            "city": address.get("localidade") or "",
            "street": address.get("logradouro") or "",
            "uf": address.get("uf") or "",
            "complement": address.get("complemento") or "",
        }

    if response.status_code == 400:
        raise exceptions.InvalidCEP()

    raise exceptions.BrazilCEPException(f"Other error. Status code: {response.status_code}")
