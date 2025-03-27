"""
brazilcep.client
~~~~~~~~~~~~~~~~~

This module implements the BrazilCEP client, which provides functionality
to query address information based on Brazilian postal codes (CEP) using
various web services.

Main Features:
- Synchronous and asynchronous methods to fetch address data.
- Support for multiple web services: ViaCEP, ApiCEP, and OpenCEP.
- Automatic formatting of CEP input to ensure valid queries.
- Customizable timeout and proxy support for HTTP requests.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

import enum
import re
from typing import Callable, Optional

from . import apicep, opencep, viacep

NUMBERS = re.compile(r"[^0-9]")
DEFAULT_TIMEOUT: int = 5  # in seconds


class WebService(enum.Enum):
    """Enum representing the available web services for CEP queries.

    Attributes:
        VIACEP: ViaCEP web service.
        APICEP: ApiCEP web service.
        OPENCEP: OpenCEP web service.
    """

    VIACEP = 1
    APICEP = 2
    OPENCEP = 3


services: dict[WebService, Callable] = {
    WebService.VIACEP: viacep.fetch_address,
    WebService.APICEP: apicep.fetch_address,
    WebService.OPENCEP: opencep.fetch_address,
}

async_services: dict[WebService, Callable] = {
    WebService.VIACEP: viacep.async_fetch_address,
    WebService.APICEP: apicep.async_fetch_address,
    WebService.OPENCEP: opencep.async_fetch_address,
}


def get_address_from_cep(
    cep: str,
    webservice: WebService = WebService.OPENCEP,
    timeout: Optional[int] = DEFAULT_TIMEOUT,
    proxies: Optional[dict] = None,
) -> dict:
    """
    This function queries a specified web service to retrieve address information
    based on the provided CEP. It supports multiple web services and allows customization
    of request parameters such as timeout and proxy settings.

    Args:
        cep (str): The CEP (Brazilian postal code) to query. Must be a valid 8-digit string.
        webservice (WebService, optional): The web service to use for the query. Defaults to WebService.OPENCEP.
            Supported values are:
            - WebService.OPENCEP
            - WebService.VIACEP
            - WebService.APICEP        timeout (Optional[int]): Timeout in seconds for the request. Defaults to 5 seconds.
        timeout (Optional[int], optional): The maximum time, in seconds, to wait for a response. Defaults to 5 seconds.
        proxies (Optional[dict], optional): A dictionary mapping protocols (e.g., "http", "https") to proxy URLs.

    Raises:
        ValueError: If the provided CEP is invalid (e.g., not properly formatted or not 8 digits).
        KeyError: If the specified webservice is not a valid WebService enum value.

    Returns:
        dict: A dictionary containing the address data corresponding to the queried CEP.

    Examples:
        >>> address = get_address_from_cep("01001000", webservice=WebService.VIACEP)
        >>> print(address)
        {
            "cep": "01001000",
            "street": "Praça da Sé",
            "complement": "lado ímpar",
            "disctric": "Sé",
            "city": "São Paulo",
            "uf": "SP",
        }
    """
    return services[webservice](_format_cep(cep), timeout=timeout, proxies=proxies)


async def async_get_address_from_cep(
    cep: str,
    webservice: WebService = WebService.OPENCEP,
    timeout: Optional[int] = DEFAULT_TIMEOUT,
    proxies: Optional[dict] = None,
) -> dict:
    """
    Asynchronously fetch the address associated with a given CEP (Brazilian postal code).

    This function queries a specified web service to retrieve address information
    based on the provided CEP. It supports multiple web services and allows customization
    of request parameters such as timeout and proxy settings.

    Args:
        cep (str): The CEP (Brazilian postal code) to query. Must be a valid 8-digit string.
        webservice (WebService, optional): The web service to use for the query. Defaults to WebService.OPENCEP.
            Supported values are:
            - WebService.OPENCEP
            - WebService.VIACEP
            - WebService.APICEP
        timeout (Optional[int], optional): The maximum time, in seconds, to wait for a response. Defaults to 5 seconds.
        proxies (Optional[dict], optional): A dictionary mapping protocols (e.g., "http", "https") to proxy URLs.

    Raises:
        ValueError: If the provided CEP is invalid (e.g., not properly formatted or not 8 digits).
        KeyError: If the specified webservice is not a valid WebService enum value.

    Returns:
        dict: A dictionary containing the address data corresponding to the queried CEP.

    Examples:
        >>> address = await async_get_address_from_cep("01001000", webservice=WebService.VIACEP)
        >>> print(address)
        {
            "cep": "01001000",
            "street": "Praça da Sé",
            "complement": "lado ímpar",
            "disctric": "Sé",
            "city": "São Paulo",
            "uf": "SP",
        }
    """
    return await async_services[webservice](_format_cep(cep), timeout=timeout, proxies=proxies)


def _format_cep(cep: str) -> str:
    """
    Format a Brazilian postal code (CEP) by removing non-numeric characters and validating its structure.

    This function ensures that the input is a valid CEP by stripping out any characters that are not digits.

    Args:
        cep (str): CEP to be formatted.

    Raises:
        ValueError: If the input is not a string or is empty.

    Returns:
        str: A string containing the formatted CEP.
    """
    if not isinstance(cep, str) or not cep.strip():
        raise ValueError("CEP must be a non-empty string.")

    return NUMBERS.sub("", cep)
