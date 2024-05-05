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
import warnings

from . import apicep, viacep

NUMBERS = re.compile(r"[^0-9]")
DEFAULT_TIMEOUT = 5  # in seconds


class WebService(enum.Enum):
    """Enum with the webservices available for consultation.

    Note: These values are passed as an argument to
    CEP query method.
    """

    CORREIOS = 0
    VIACEP = 1
    APICEP = 2


services = {
    WebService.CORREIOS: None,
    WebService.VIACEP: viacep.fetch_address,
    WebService.APICEP: apicep.fetch_address,
}


def get_address_from_cep(cep, webservice=WebService.APICEP, timeout=None, proxies=None):
    """Returns the address corresponding to the zip (cep) code entered.

    Args:
        cep (str): CEP to be queried.
        timeout (int): How many seconds to wait for the server to return data before giving up.
        proxies (dict):  Dictionary mapping protocol to the URL of the proxy.

    Raises:
        RequestError: When connection error occurs in CEP query
        Timeout: When occurs timeout of webservice response
        HTTPError: Invalid HTTP format query
        CEPNotFund: CEP not exist in API
        Exception: When any error occurs in the CEP query

    returns:
        address (dict): Address data of the queried CEP.

    """

    if webservice not in (value for _, value in WebService.__dict__.items()):
        raise KeyError(
            """Invalid webservice. Please use this options:
        WebService.VIACEP, WebService.APICEP
    """
        )

    if webservice == WebService.CORREIOS:
        warnings.warn(
            "CORREIOS support has been deprecated, and we intend to remove it"
            " in a future release of BrazilCEP. Please use the WebService.VIACEP, WebService.APICEP"
            " instead, as described in the documentation.",
            DeprecationWarning,
        )

        # override deprecated option
        webservice = WebService.APICEP

    kwargs = {}

    if timeout and isinstance(timeout, int):
        kwargs["timeout"] = timeout

    if proxies and isinstance(proxies, dict):
        kwargs["proxies"] = proxies

    return services[webservice](_format_cep(cep), **kwargs)


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
