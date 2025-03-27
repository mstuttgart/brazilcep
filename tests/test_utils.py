from unittest.mock import AsyncMock, MagicMock, patch

import aiohttp
import pytest
import requests

from brazilcep import exceptions, utils

URL = "https://api.com/99999999"


# sync tests


def test_requests_get_timeout_error(requests_mock):
    """
    Test requests_get with a timeout error.
    """

    requests_mock.get(URL, exc=requests.exceptions.Timeout)

    with pytest.raises(exceptions.Timeout):
        utils.requests_get(URL)


def test_connection_error(requests_mock):
    """
    Test requests_get with a connection error.
    """
    requests_mock.get(URL, exc=requests.exceptions.ConnectionError)

    with pytest.raises(exceptions.ConnectionError):
        utils.requests_get(URL)


def test_http_error(requests_mock):
    """
    Test requests_get with a HTTP error.
    """
    requests_mock.get(URL, exc=requests.exceptions.HTTPError)

    with pytest.raises(exceptions.HTTPError):
        utils.requests_get(URL)


def test_url_required_error(requests_mock):
    """
    Test requests_get with a URL required error.
    """
    requests_mock.get(URL, exc=requests.exceptions.URLRequired)

    with pytest.raises(exceptions.URLRequired):
        utils.requests_get(URL)


def test_too_many_redirects_error(requests_mock):
    """
    Test requests_get with a too many redirects error.
    """
    requests_mock.get(URL, exc=requests.exceptions.TooManyRedirects)

    with pytest.raises(exceptions.TooManyRedirects):
        utils.requests_get(URL)


def test_general_exception_error(requests_mock):
    """
    Test requests_get with a general_exception error.
    """
    requests_mock.get(URL, exc=Exception)

    with pytest.raises(exceptions.BrazilCEPException):
        utils.requests_get(URL)


# async tests


@pytest.mark.asyncio
async def test_aiohttp_get_success():
    """
    Test aiohttp_get with a successful response.
    """

    mock_response = MagicMock()
    mock_response.status = 200
    mock_response.text = AsyncMock(return_value="Success")
    mock_response.__aenter__.return_value = mock_response

    with patch("brazilcep.utils.aiohttp.ClientSession.get", return_value=mock_response):
        status, text = await utils.aiohttp_get(URL)
        assert status == 200
        assert text == "Success"


@pytest.mark.asyncio
async def test_aiohttp_get_connection_error():
    """
    Test aiohttp_get with a connection error.
    """

    with patch(
        "brazilcep.utils.aiohttp.ClientSession.get", side_effect=aiohttp.ClientConnectionError
    ):
        with pytest.raises(exceptions.ConnectionError):
            await utils.aiohttp_get(URL)


@pytest.mark.asyncio
async def test_aiohttp_get_timeout():
    """
    Test aiohttp_get with a timeout error.
    """

    with patch(
        "brazilcep.utils.aiohttp.ClientSession.get", side_effect=aiohttp.ConnectionTimeoutError
    ):
        with pytest.raises(exceptions.Timeout):
            await utils.aiohttp_get(URL, timeout=1)


@pytest.mark.asyncio
async def test_aiohttp_get_client_error():
    """
    Test aiohttp_get with a client error.
    """

    with patch("brazilcep.utils.aiohttp.ClientSession.get", side_effect=aiohttp.ClientError):
        with pytest.raises(exceptions.BrazilCEPException):
            await utils.aiohttp_get(URL)


@pytest.mark.asyncio
async def test_aiohttp_get_general_exception():
    """
    Test aiohttp_get with a general exception.
    """

    with patch("brazilcep.utils.aiohttp.ClientSession.get", side_effect=Exception):
        with pytest.raises(exceptions.BrazilCEPException):
            await utils.aiohttp_get(URL)


@pytest.mark.asyncio
async def test_raise_for_status():
    """
    Test aiohttp_get with raise_for_status response.
    """

    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock(side_effect=aiohttp.ClientResponseError)
    mock_response.__aenter__.return_value = mock_response

    with patch("brazilcep.utils.aiohttp.ClientSession.get", return_value=mock_response):
        with pytest.raises(exceptions.BrazilCEPException):
            await utils.aiohttp_get(URL, raise_for_status=True)
