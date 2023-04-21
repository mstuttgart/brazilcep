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

from . import apicep, correios, viacep

NUMBERS = re.compile(r"[^0-9]")


class WebService(enum.Enum):
    """Enum with the webservices available for consultation.

    Note: These values are passed as an argument to
    CEP query method.
    """

    CORREIOS = 0
    VIACEP = 1
    APICEP = 2


services = {
    WebService.CORREIOS: correios.fetch_address,
    WebService.VIACEP: viacep.fetch_address,
    WebService.APICEP: apicep.fetch_address,
}


def get_address_from_cep(cep, webservice=WebService.APICEP):
    """Returns the address corresponding to the zip (cep) code entered.

    Args:
        cep (str): CEP to be queried.

    Raises:
        RequestError: When connection error occurs in CEP query
        Timeout: When occurs timeout of webservice response
        HTTPError: Invalid HTTP format query
        CEPNotFund: CEP not exist in API
        Exception: When any error occurs in the CEP query

    returns:
        address (dict): Address data of the queried CEP.

    """

    if webservice not in (value for attribute, value in WebService.__dict__.items()):
        raise KeyError(
            """Invalid webservice. Please use this options:
        WebService.CORREIOS, WebService.VIACEP, WebService.APICEP
    """
        )

    cep = _format_cep(cep)

    return services[webservice](_format_cep(cep))


def _format_cep(cep):
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
