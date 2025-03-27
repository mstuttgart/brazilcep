"""
brazilcep.opencep
~~~~~~~~~~~~~~~~~

This module provides an adapter for the BrazilCEP library to interact with the OpenCEP API.

The OpenCEP API is a RESTful web service that allows querying Brazilian postal codes (CEPs)
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

URL = "https://opencep.com/v1/{}"


def __format_response(response: dict) -> dict:
    """
    Formats the response from the OpenCEP API into a standardized address dictionary.

    This function processes the raw JSON response from the OpenCEP API and extracts
    relevant address fields, ensuring that all string values are stripped of leading
    and trailing whitespace. If a field is missing in the response, it defaults to
    an empty string.

    Args:
        response (dict): The raw JSON response from the OpenCEP API.

    Returns:

        dict: A dictionary containing the following standardized address fields:
            - district (str): The neighborhood or district name (from "bairro").
            - cep (str): The postal code (from "cep").
            - city (str): The city name (from "localidade").
            - street (str): The street name (from "logradouro").
            - uf (str): The state abbreviation (from "uf").
            - complement (str): Additional address details (from "complemento").
    """

    return {
        "district": response.get("bairro") or "",
        "cep": response.get("cep") or "",
        "city": response.get("localidade") or "",
        "street": response.get("logradouro") or "",
        "uf": response.get("uf") or "",
        "complement": "",
    }


def __handle_response(status_code: int, text: str) -> dict:
    """
    Handles the API response based on the status code and response content.

    Args:
        status_code (int): The HTTP status code returned by the API.
        text (str): The raw response content from the API.

    Raises:
        exceptions.CEPNotFound: If the CEP is not found (404 status code).
        exceptions.BrazilCEPException: For any other non-successful status codes.

    Returns:
        dict: A formatted dictionary containing address information if the request is successful.
    """
    try:
        if status_code == 200:
            response_json = json.loads(text)
            return __format_response(response_json)

        if status_code == 404:
            raise exceptions.CEPNotFound()

        raise exceptions.BrazilCEPException(f"Unexpected error. Status code: {status_code}")

    except json.JSONDecodeError as e:
        raise exceptions.BrazilCEPException(f"Failed to parse JSON response: {e}")


def fetch_address(
    cep: str, timeout: Union[None, int] = None, proxies: Union[None, dict] = None
) -> dict:
    """
    Fetch address data from the OpenCEP API using a given CEP.

    This function queries the OpenCEP REST API to retrieve address information
    for a given Brazilian postal code (CEP). It handles various exceptions and
    returns a standardized address dictionary.

    Args:
        cep (str): The CEP to be searched.
        timeout (Union[None, int], optional): The number of seconds to wait for the server to respond. Defaults to None.
        proxies (Union[None, dict], optional): A dictionary mapping protocol to the URL of the proxy. Defaults to None.

    Raises:
        exceptions.ConnectionError: Raised for connection errors.
        exceptions.HTTPError: Raised for HTTP errors.
        exceptions.URLRequired: Raised for invalid URLs.
        exceptions.TooManyRedirects: Raised for too many redirects.
        exceptions.Timeout: Raised when the request times out.
        exceptions.InvalidCEP: Raised for invalid CEP requests.
        exceptions.CEPNotFound: Raised when the CEP is not found.
        exceptions.BrazilCEPException: Base class for other exceptions.

    Returns:
        dict: A dictionary containing standardized address data.
    """
    status_code, text = utils.requests_get(url=URL.format(cep), timeout=timeout, proxies=proxies)
    return __handle_response(status_code=status_code, text=text)


async def async_fetch_address(
    cep: str, timeout: Union[None, int] = None, proxies: Union[None, dict] = None
) -> dict:
    """
    Fetch address data asynchronously from the OpenCEP API using a given CEP.

    This function queries the OpenCEP REST API asynchronously to retrieve address information
    for a given Brazilian postal code (CEP). It handles various exceptions and
    returns a standardized address dictionary.

    Args:
        cep (str): The CEP to be searched.
        timeout (Union[None, int], optional): The number of seconds to wait for the server to respond. Defaults to None.
        proxies (Union[None, dict], optional): A dictionary mapping protocol to the URL of the proxy. Defaults to None.

    Raises:
        exceptions.ConnectionError: Raised for connection errors.
        exceptions.HTTPError: Raised for HTTP errors.
        exceptions.URLRequired: Raised for invalid URLs.
        exceptions.TooManyRedirects: Raised for too many redirects.
        exceptions.Timeout: Raised when the request times out.
        exceptions.InvalidCEP: Raised for invalid CEP requests.
        exceptions.CEPNotFound: Raised when the CEP is not found.
        exceptions.BrazilCEPException: Base class for other exceptions.

    Returns:
        dict: A dictionary containing standardized address data.
    """
    status_code, text = await utils.aiohttp_get(url=URL.format(cep), timeout=timeout)
    return __handle_response(status_code=status_code, text=text)
