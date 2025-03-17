from typing import Union

import aiohttp
import requests

from . import exceptions


async def aiohttp_get(
    url: str, timeout: Union[None, int], raise_for_status: bool = False
) -> tuple[int, str]:
    try:
        async with aiohttp.ClientSession() as session:
            base_timeout = aiohttp.ClientTimeout(30)
            if timeout:
                base_timeout = aiohttp.ClientTimeout(timeout)

            async with session.get(url, timeout=base_timeout) as response:
                if raise_for_status:
                    response.raise_for_status()
                response_text = await response.text()
                return response.status, response_text
    # TODO: Aplicar tratamento de erros
    except Exception as exc:
        raise exceptions.HTTPError(exc)


def requests_get(
    url: str, timeout: Union[None, int], proxies: Union[None, dict]
) -> tuple[int, str]:
    """Execute `requests.get` and applies exception handling


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
        The JSON Response from the endpoint
    """
    try:
        response = requests.get(url, timeout=timeout, proxies=proxies)

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

    return response.status_code, response.text
