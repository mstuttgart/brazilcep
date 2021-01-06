import pytest
import requests

from pycep_correios import WebService, exceptions, get_address_from_cep


def test_get_address_from_cep_success():

    # Realizamos a consulta de CEP
    address = get_address_from_cep('37.503-130', webservice=WebService.VIACEP)

    assert address['bairro'] == 'Santo Antônio'
    assert address['cep'] == '37503-130'
    assert address['cidade'] == 'Itajubá'
    assert address['complemento'] == 'até 214/215'
    assert address['logradouro'] == 'Rua Geraldino Campista'
    assert address['uf'] == 'MG'


def test_get_address_from_cep_fail():

    # Realizamos a consulta de CEP
    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep('00000-000', webservice=WebService.VIACEP)

    with pytest.raises(exceptions.InvalidCEP):
        get_address_from_cep('37503-13', webservice=WebService.VIACEP)


def test_fetch_address_404(requests_mock):

    requests_mock.get('http://www.viacep.com.br/ws/37503130/json', status_code=404)  # noqa

    with pytest.raises(exceptions.BaseException):
        get_address_from_cep('37503-130', webservice=WebService.VIACEP)


def test_fetch_address_connection_error(requests_mock):

    requests_mock.get('http://www.viacep.com.br/ws/37503130/json', exc=requests.exceptions.ConnectTimeout)  # noqa

    with pytest.raises(exceptions.ConnectionError):
        get_address_from_cep('37503-130', webservice=WebService.VIACEP)


def test_fetch_address_timeout(requests_mock):

    requests_mock.get('http://www.viacep.com.br/ws/37503130/json', exc=requests.exceptions.Timeout)  # noqa

    with pytest.raises(exceptions.Timeout):
        get_address_from_cep('37503-130', webservice=WebService.VIACEP)


def test_fetch_address_http_error(requests_mock):

    requests_mock.get('http://www.viacep.com.br/ws/37503130/json', exc=requests.exceptions.HTTPError)  # noqa

    with pytest.raises(exceptions.HTTPError):
        get_address_from_cep('37503-130', webservice=WebService.VIACEP)


def test_fetch_address_request_exception(requests_mock):

    requests_mock.get('http://www.viacep.com.br/ws/37503130/json', exc=requests.exceptions.RequestException)  # noqa

    with pytest.raises(exceptions.BaseException):
        get_address_from_cep('37503-130', webservice=WebService.VIACEP)
