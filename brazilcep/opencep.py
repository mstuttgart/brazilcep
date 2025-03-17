"""
brazilcep.opencep
~~~~~~~~~~~~~~~~

This module implements the BrazilCEP ApiCEP adapter.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

import json
from typing import Union

from . import exceptions
from .utils import aiohttp_get, requests_get

URL = "https://opencep.com/v1/{}"


def __format_response(response: dict) -> dict:
    """Formats the OpenCEP API response

    Args:
        response: The API JSON response

    Returns:
        Address data from the API JSON response
    """

    return {
        "district": response.get("bairro") or "",
        "cep": response.get("cep") or "",
        "city": response.get("localidade") or "",
        "street": response.get("logradouro") or "",
        "uf": response.get("uf") or "",
        "complement": "",
    }


def __handle_response(status_code: int, text: str):
    """Handle response from API based on status_code and text (content of the response)"""
    if status_code == 200:
        response_json = json.loads(text)
        return __format_response(response_json)

    if status_code == 404:
        raise exceptions.CEPNotFound()

    else:
        raise exceptions.BrazilCEPException(f"Other error. Status code: {status_code}")


def fetch_address(cep: str, timeout: Union[None, int], proxies: Union[None, dict]) -> dict:
    """Fetch OpenCEP webservice for CEP address. OpenCEP provide
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

    status_code, text = requests_get(url=URL.format(cep), timeout=timeout, proxies=proxies)
    return __handle_response(status_code=status_code, text=text)


async def async_fetch_address(
    cep: str, timeout: Union[None, int], proxies: Union[None, dict]
) -> dict:
    status_code, text = await aiohttp_get(URL.format(cep), timeout=timeout, raise_for_status=True)
    return __handle_response(status_code=status_code, text=text)


async_fetch_address.__doc__ = fetch_address.__doc__
