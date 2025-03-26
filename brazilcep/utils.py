from typing import Optional

import aiohttp
import requests

from . import exceptions


async def aiohttp_get(
    url: str, timeout: Optional[int] = None, raise_for_status: bool = False
) -> tuple[int, str]:
    """Perform an asynchronous GET request using aiohttp.

    Args:
        url (str): The URL to request.
        timeout (Optional[int]): Timeout in seconds for the request.
        raise_for_status (bool): Whether to raise an exception for HTTP errors.

    Returns:
        tuple[int, str]: The HTTP status code and response text.

    Raises:
        exceptions.HTTPError: Raised for any exception during the request.
    """
    try:
        client_timeout = aiohttp.ClientTimeout(total=timeout or 30)

        async with aiohttp.ClientSession(timeout=client_timeout) as session:
            async with session.get(url) as response:
                if raise_for_status:
                    response.raise_for_status()

                response_text = await response.text()
                return response.status, response_text

    except aiohttp.ClientError as exc:
        raise exceptions.HTTPError(exc)

    except Exception as exc:
        raise exceptions.HTTPError(exc)


def requests_get(
    url: str, timeout: Optional[int] = None, proxies: Optional[dict] = None
) -> tuple[int, str]:
    """
    Perform a synchronous GET request using requests.

    Args:
        url (str): The URL to request.
        timeout (Optional[int]): Timeout in seconds for the request.
        proxies (Optional[dict]): Proxy configuration for the request.

    Returns:
        tuple[int, str]: The HTTP status code and response text.

    Raises:
        exceptions.ConnectionError: Raised for connection errors.
        exceptions.HTTPError: Raised for HTTP errors.
        exceptions.URLRequired: Raised for invalid URLs.
        exceptions.TooManyRedirects: Raised for too many redirects.
        exceptions.Timeout: Raised for request timeouts.
    """
    try:
        response = requests.get(url, timeout=timeout, proxies=proxies)
        return response.status_code, response.text

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

    except Exception as exc:
        raise exceptions.HTTPError(exc)
