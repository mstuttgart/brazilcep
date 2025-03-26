"""
brazilcep.client
~~~~~~~~~~~~~~~~

This module implements the BrazilCEP client.
This is the main module of BrazilCEP.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

import enum
import re
from typing import Optional
from warnings import warn

from . import apicep, opencep, viacep

NUMBERS = re.compile(r"[^0-9]")
DEFAULT_TIMEOUT: int = 5  # in seconds


class WebService(enum.Enum):
    """Enum with the webservices available for consultation.

    Note: These values are passed as an argument to
    CEP query method.
    """

    CORREIOS = 0
    VIACEP = 1
    APICEP = 2
    OPENCEP = 3


services: dict = {
    # TOFIX: compatibility adjust. remove CORREIOS in next version
    WebService.CORREIOS: opencep.fetch_address,
    WebService.VIACEP: viacep.fetch_address,
    WebService.APICEP: apicep.fetch_address,
    WebService.OPENCEP: opencep.fetch_address,
}

async_services: dict = {
    # TOFIX: compatibility adjust. remove CORREIOS in next version
    WebService.CORREIOS: opencep.async_fetch_address,
    WebService.VIACEP: viacep.async_fetch_address,
    WebService.APICEP: apicep.async_fetch_address,
    WebService.OPENCEP: opencep.async_fetch_address,
}


def get_address_from_cep(
    cep: str,
    webservice: WebService = WebService.OPENCEP,
    timeout: Optional[int] = None,
    proxies: Optional[dict] = None,
) -> dict:
    """Returns the address corresponding to the zip (cep) code entered

    Args:
        cep: CEP to be queried
        webservice: enum to webservice APIs
        timeout: How many seconds to wait for the server to return data before giving up
        proxies:  Dictionary mapping protocol to the URL of the proxy

    Raises:
        KeyError: raise if `webservice` parameter is a invalid webservice enum value

    Returns:
        Address data of the queried CEP
    """

    if webservice == WebService.CORREIOS:
        warn(
            "CORREIOS is going to be deprecated. Please, use other webservice.",
            DeprecationWarning,
            stacklevel=2,
        )

    if webservice not in (value for _, value in WebService.__dict__.items()):
        raise KeyError(
            """Invalid webservice. Please use this options: WebService.VIACEP, WebService.APICEP or WebService.OPENCEP"""
        )

    return services[webservice](_format_cep(cep), timeout=timeout, proxies=proxies)


async def async_get_address_from_cep(
    cep: str,
    webservice: WebService = WebService.OPENCEP,
    timeout: Optional[int] = None,
    proxies: Optional[dict] = None,
) -> dict:
    if webservice == WebService.CORREIOS:
        warn(
            "CORREIOS is going to be deprecated. Please, use other webservice.",
            DeprecationWarning,
            stacklevel=2,
        )

    if webservice not in (value for _, value in WebService.__dict__.items()):
        raise KeyError(
            """Invalid webservice. Please use this options: WebService.VIACEP, WebService.APICEP or WebService.OPENCEP"""
        )

    return await async_services[webservice](_format_cep(cep), timeout=timeout, proxies=proxies)


async_get_address_from_cep.__doc__ = get_address_from_cep.__doc__


def _format_cep(cep: str) -> str:
    """Format CEP, removing any non-numeric characters.

    Args:
        cep (str): CEP to be formatted.

    Raises:
        ValueError: When the string is empty or does not contain numbers.

    returns:
        cep (str): string containing the formatted CEP.
    """
    if not isinstance(cep, str) or not cep:
        raise ValueError("CEP must be a non-empty string containing only numbers")

    return NUMBERS.sub("", cep)
