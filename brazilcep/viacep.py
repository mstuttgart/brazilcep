"""
brazilcep.viacep
~~~~~~~~~~~~~~~~

This module provides an adapter for the BrazilCEP library to interact with the ViaCEP API.

The ViaCEP API is a RESTful web service that allows querying Brazilian postal codes (CEPs)
to retrieve address information. This module includes both synchronous and asynchronous
functions for fetching address data, handling API responses, and formatting the results.

Features:
- Fetch address data using a CEP (postal code).
- Handle API responses and errors gracefully.
- Support for both synchronous and asynchronous operations.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

import json
from typing import Union

from . import exceptions, utils

URL = "http://www.viacep.com.br/ws/{}/json"


def __format_response(response: dict) -> dict:
    """
    Transforms the raw ViaCEP API response into a standardized address dictionary.

    This function extracts and formats specific fields from the API response,
    ensuring that all string values are stripped of leading and trailing whitespace.

    Args:
        response (dict): The raw JSON response from the ViaCEP API.

    Returns:
        dict: A dictionary containing the following standardized address fields:
            - district (str): The neighborhood or district name.
            - cep (str): The postal code (CEP).
            - city (str): The city name.
            - street (str): The street name.
            - uf (str): The state abbreviation (UF).
            - complement (str): Additional address information, if available.
    """

    return {
        "district": response.get("bairro") or "",
        "cep": response.get("cep") or "",
        "city": response.get("localidade") or "",
        "street": response.get("logradouro") or "",
        "uf": response.get("uf") or "",
        "complement": response.get("complemento") or "",
    }


def __handle_response(status_code: int, text: str) -> dict:
    """
    Handles the API response based on the status code and response content.

    Args:
        status_code (int): The HTTP status code returned by the API.
        text (str): The raw response content from the API.

    Raises:
        exceptions.CEPNotFound: If the CEP is not found in the API response.
        exceptions.InvalidCEP: If the provided CEP is invalid.
        exceptions.BrazilCEPException: For any other errors with the API response.

    Returns:
        dict: A formatted dictionary containing address information.
    """
    if status_code == 200:
        try:
            response_json = json.loads(text)
        except json.JSONDecodeError as e:
            raise exceptions.BrazilCEPException(f"Invalid JSON response: {e}")

        if response_json.get("erro"):
            raise exceptions.CEPNotFound("CEP not found in the API response.")

        return __format_response(response_json)

    if status_code == 400:
        raise exceptions.InvalidCEP("The provided CEP is invalid.")

    raise exceptions.BrazilCEPException(f"Unexpected error. Status code: {status_code}")


def fetch_address(
    cep: str, timeout: Union[None, int] = None, proxies: Union[None, dict] = None
) -> dict:
    """
    Fetch address information for a given CEP using the ViaCEP API.

    This function sends a synchronous HTTP request to the ViaCEP API to retrieve
    address information for the specified CEP (postal code).

    Args:
        cep (str): The CEP to be searched.
        timeout (Union[None, int], optional): The number of seconds to wait for the server to respond. Defaults to None.
        proxies (Union[None, dict], optional): A dictionary mapping protocol to the URL of the proxy. Defaults to None.

    Raises:
        exceptions.ConnectionError: Raised for connection errors.
        exceptions.HTTPError: Raised for HTTP errors.
        exceptions.URLRequired: Raised if an invalid URL is used for the request.
        exceptions.TooManyRedirects: Raised if too many redirects occur.
        exceptions.Timeout: Raised if the request times out.
        exceptions.InvalidCEP: Raised if the provided CEP is invalid.
        exceptions.CEPNotFound: Raised if the CEP is not found in the API response.
        exceptions.BrazilCEPException: Base class for other exceptions.

    Returns:
        dict: A dictionary containing standardized address information.
    """
    status_code, text = utils.requests_get(url=URL.format(cep), timeout=timeout, proxies=proxies)
    return __handle_response(status_code=status_code, text=text)


async def async_fetch_address(
    cep: str, timeout: Union[None, int] = None, proxies: Union[None, dict] = None
) -> dict:
    """
    Fetch address information for a given CEP asynchronously using the ViaCEP API.

    This function sends an asynchronous HTTP request to the ViaCEP API to retrieve
    address information for the specified CEP (postal code).

    Args:
        cep (str): The CEP to be searched.
        timeout (Union[None, int], optional): The number of seconds to wait for the server to respond. Defaults to None.
        proxies (Union[None, dict], optional): A dictionary mapping protocol to the URL of the proxy. Defaults to None.

    Raises:
        exceptions.ConnectionError: Raised for connection errors.
        exceptions.HTTPError: Raised for HTTP errors.
        exceptions.URLRequired: Raised if an invalid URL is used for the request.
        exceptions.TooManyRedirects: Raised if too many redirects occur.
        exceptions.Timeout: Raised if the request times out.
        exceptions.InvalidCEP: Raised if the provided CEP is invalid.
        exceptions.CEPNotFound: Raised if the CEP is not found in the API response.
        exceptions.BrazilCEPException: Base class for other exceptions.

    Returns:
        dict: A dictionary containing standardized address information.
    """
    status_code, text = await utils.aiohttp_get(url=URL.format(cep), timeout=timeout)
    return __handle_response(status_code=status_code, text=text)
