import pytest
import requests

from pycep_correios import WebService, exceptions, get_address_from_cep


def test_fetch_address_success(requests_mock):

    req_mock_text = ('''{
        "status":200,
        "ok":true,
        "code":"37503-130",
        "state":"MG",
        "city":"Itajubá",
        "district":"Santo Antônio",
        "address":"Rua Geraldino Campista - até 214/215",
        "statusText":"ok"
    }''')

    requests_mock.get(
        'https://ws.apicep.com/cep/37503130.json', text=req_mock_text)

    # Realizamos a consulta de CEP
    address = get_address_from_cep('37.503-130', webservice=WebService.APICEP)

    assert address['bairro'] == 'Santo Antônio'
    assert address['cep'] == '37503-130'
    assert address['cidade'] == 'Itajubá'
    assert address['complemento'] == ''
    assert address['logradouro'] == 'Rua Geraldino Campista'
    assert address['uf'] == 'MG'

    req_mock_text = ('''{
        "status":200,
        "ok":true,
        "code":"99999-999",
        "state":"PR",
        "city":"Sarandi",
        "district":null,
        "address":null,
        "statusText":"ok"
    }''')

    requests_mock.get(
        'https://ws.apicep.com/cep/99999999.json', text=req_mock_text)

    # Realizamos a consulta de CEP
    address = get_address_from_cep('99999-999', webservice=WebService.APICEP)

    assert address['bairro'] == ''
    assert address['cep'] == '99999-999'
    assert address['cidade'] == 'Sarandi'
    assert address['complemento'] == ''
    assert address['logradouro'] == ''
    assert address['uf'] == 'PR'


def test_fetch_address_cep_not_found(requests_mock):

    req_mock_text = ('''{
        "status":404
    }''')

    requests_mock.get(
        'https://ws.apicep.com/cep/00000000.json', text=req_mock_text)

    # Realizamos a consulta de CEP
    with pytest.raises(exceptions.CEPNotFound):
        get_address_from_cep('00000-000', webservice=WebService.APICEP)


def test_fetch_address_invalid_cep(requests_mock):

    req_mock_text = ('''{
        "status":400,
        "message": "CEP informado é inválido"
    }''')

    requests_mock.get(
        'https://ws.apicep.com/cep/3750313.json', text=req_mock_text)

    with pytest.raises(exceptions.InvalidCEP):
        get_address_from_cep('37503-13', webservice=WebService.APICEP)


def test_fetch_address_blocked_by_flood(requests_mock):

    req_mock_text = ('''{
        "status":400,
        "message": "Blocked by flood"
    }''')

    requests_mock.get(
        'https://ws.apicep.com/cep/3750313.json', text=req_mock_text)

    with pytest.raises(exceptions.BlockedByFlood):
        get_address_from_cep('37503-13', webservice=WebService.APICEP)


def test_fetch_address_404(requests_mock):

    requests_mock.get('https://ws.apicep.com/cep/37503130.json', status_code=404)  # noqa

    with pytest.raises(exceptions.BaseException):
        get_address_from_cep('37503-130', webservice=WebService.APICEP)


def test_fetch_address_connection_error(requests_mock):

    requests_mock.get('https://ws.apicep.com/cep/37503130.json', exc=requests.exceptions.ConnectTimeout)  # noqa

    with pytest.raises(exceptions.ConnectionError):
        get_address_from_cep('37503-130', webservice=WebService.APICEP)


def test_fetch_address_timeout(requests_mock):

    requests_mock.get('https://ws.apicep.com/cep/37503130.json', exc=requests.exceptions.Timeout)  # noqa

    with pytest.raises(exceptions.Timeout):
        get_address_from_cep('37503-130', webservice=WebService.APICEP)


def test_fetch_address_http_error(requests_mock):

    requests_mock.get('https://ws.apicep.com/cep/37503130.json', exc=requests.exceptions.HTTPError)  # noqa

    with pytest.raises(exceptions.HTTPError):
        get_address_from_cep('37503-130', webservice=WebService.APICEP)


def test_fetch_address_request_exception(requests_mock):

    requests_mock.get('https://ws.apicep.com/cep/37503130.json', exc=requests.exceptions.RequestException)  # noqa

    with pytest.raises(exceptions.BaseException):
        get_address_from_cep('37503-130', webservice=WebService.APICEP)
