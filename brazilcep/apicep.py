"""
brazilcep.apicep
~~~~~~~~~~~~~~~~

This module provides an adapter for the BrazilCEP library to interact with the ApiCEP API.

The ApiCEP API is a RESTful web service that allows querying Brazilian postal codes (CEPs)
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

from brazilcep import exceptions, utils

URL = "https://ws.apicep.com/cep/{}.json"


def __format_response(response: dict) -> dict:
    """
    Formats the response from the ApiCEP API into a standardized address dictionary.

    This function processes the raw JSON response from the ApiCEP API and extracts
    relevant address information, ensuring that all fields are properly formatted
    and stripped of unnecessary whitespace.

    Args:
        response (dict): The raw JSON response from the ApiCEP API

    Returns:
        A dictionary containing the formatted address data.

        dict: A dictionary containing the formatted address data with the following keys:
            - district (str): The neighborhood or district name.
            - cep (str): The postal code (CEP).
            - city (str): The name of the city.
            - street (str): The street name, excluding any additional information.
            - uf (str): The state abbreviation (e.g., "SP" for São Paulo).
            - complement (str): Additional address details, if available.
    """

    return {
        "district": response.get("district") or "",
        "cep": response.get("code") or "",
        "city": response.get("city") or "",
        "street": (response.get("address") or "").split(" - até")[0],
        "uf": response.get("state") or "",
        "complement": "",
    }


def __handle_response(status_code: int, text: str):
    """
    Handles the API response based on the HTTP status code and response content.

    Args:
        status_code (int): The HTTP status code returned by the API.
        text (str): The raw response content as a string.

    Raises:
        exceptions.BrazilCEPException: If the JSON response cannot be parsed or an unexpected error occurs.
        exceptions.InvalidCEP: If the API indicates the provided CEP (postal code) is invalid.
        exceptions.BlockedByFlood: If the API blocks the request due to excessive usage (rate limiting).
        exceptions.CEPNotFound: If the API indicates the requested CEP (postal code) was not found.

    Returns:
        dict: A formatted dictionary containing the parsed and processed response data if the request is successful.
    """

    if status_code == 200:
        try:
            response_json = json.loads(text)
        except json.JSONDecodeError as e:
            raise exceptions.BrazilCEPException(f"Failed to parse JSON response: {e}")

        status = response_json.get("status")
        message = response_json.get("message")

        if status == 400:
            if message == "CEP informado é inválido":
                raise exceptions.InvalidCEP()

            if message == "Blocked by flood":
                raise exceptions.BlockedByFlood()

            raise exceptions.BrazilCEPException(
                f"Unexpected error. Status: {status}, Message: {message}"
            )

        elif status == 404:
            raise exceptions.CEPNotFound()

        else:
            return __format_response(response_json)

    elif status_code == 429:
        raise exceptions.BlockedByFlood()

    raise exceptions.BrazilCEPException(
        f"Unexpected error. Status code: {status_code}, Response: {text}"
    )


def fetch_address(
    cep: str, timeout: Union[None, int] = None, proxies: Union[None, dict] = None
) -> dict:
    """
    Fetch address data from the ApiCEP web service using a given CEP.

    This function sends a synchronous HTTP request to the ApiCEP API to retrieve
    address information for the provided CEP (Brazilian postal code).

    Args:
        cep (str): The CEP to be searched.
        timeout (Union[None, int], optional): The number of seconds to wait for the server to respond. Defaults to None.
        proxies (Union[None, dict], optional): A dictionary mapping protocol to the URL of the proxy. Defaults to None.

    Raises:
        exceptions.ConnectionError: Raised when a connection error occurs.
        exceptions.HTTPError: Raised for HTTP errors.
        exceptions.URLRequired: Raised when an invalid URL is used for the request.
        exceptions.TooManyRedirects: Raised when too many redirects occur.
        exceptions.Timeout: Raised when the request times out.
        exceptions.InvalidCEP: Raised for invalid CEP requests.
        exceptions.BlockedByFlood: Raised when the API blocks the request due to excessive usage.
        exceptions.CEPNotFound: Raised when the requested CEP is not found.
        exceptions.BrazilCEPException: Base class for other exceptions.

    Returns:
        dict: A dictionary containing the formatted address data.
    """
    status_code, text = utils.requests_get(url=URL.format(cep), timeout=timeout, proxies=proxies)
    return __handle_response(status_code=status_code, text=text)


async def async_fetch_address(
    cep: str, timeout: Union[None, int] = None, proxies: Union[None, dict] = None
) -> dict:
    """
    Fetch address data asynchronously from the ApiCEP web service using a given CEP.

    This function sends an asynchronous HTTP request to the ApiCEP API to retrieve
    address information for the provided CEP (Brazilian postal code).

    Args:
        cep (str): The CEP to be searched.
        timeout (Union[None, int], optional): The number of seconds to wait for the server to respond. Defaults to None.
        proxies (Union[None, dict], optional): A dictionary mapping protocol to the URL of the proxy. Defaults to None.

    Raises:
        exceptions.ConnectionError: Raised when a connection error occurs.
        exceptions.HTTPError: Raised for HTTP errors.
        exceptions.URLRequired: Raised when an invalid URL is used for the request.
        exceptions.TooManyRedirects: Raised when too many redirects occur.
        exceptions.Timeout: Raised when the request times out.
        exceptions.InvalidCEP: Raised for invalid CEP requests.
        exceptions.BlockedByFlood: Raised when the API blocks the request due to excessive usage.
        exceptions.CEPNotFound: Raised when the requested CEP is not found.
        exceptions.BrazilCEPException: Base class for other exceptions.

    Returns:
        dict: A dictionary containing the formatted address data.
    """

    status_code, text = await utils.aiohttp_get(url=URL.format(cep), timeout=timeout)
    return __handle_response(status_code=status_code, text=text)
