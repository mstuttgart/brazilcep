import json

import requests

from . import exceptions

URL = 'http://www.viacep.com.br/ws/{}/json'

URL_CEP_FROM_ADDRESS = 'http://www.viacep.com.br/ws/{}/{}/{}/json'


def fetch_address(cep):

    try:
        response = requests.get(URL.format(cep))

        if response.status_code == 200:

            # Transforma o objeto requests em um dict
            address = json.loads(response.text)

            if address.get('erro'):
                raise exceptions.CEPNotFound()

            return {
                'bairro': address.get('bairro', ''),
                'cep': address.get('cep', ''),
                'cidade': address.get('localidade', ''),
                'logradouro': address.get('logradouro', ''),
                'uf': address.get('uf', ''),
                'complemento': address.get('complemento', ''),
            }

        elif response.status_code == 400:
            raise exceptions.InvalidCEP()

        else:
            raise exceptions.BaseException('Other error. Status code: %d' % response.status_code)  # noqa

    except requests.exceptions.ConnectionError as errc:
        raise exceptions.ConnectionError(errc)

    except requests.exceptions.Timeout as errt:
        raise exceptions.Timeout(errt)

    except requests.exceptions.HTTPError as errh:
        raise exceptions.HTTPError(errh)

    except requests.exceptions.RequestException as e:
        raise exceptions.BaseException(e)


def fetch_cep(state, city, street):
    """Retorna os CEPs correspondente ao endereço informado.

    Arguments:
        state {str} -- Sigla do estado da consulta
        city {str} -- Cidade do CEP ser encontrado
        street {str} -- Rua do CEP a ser encontrado
    Raises:
        BaseException -- Quando ocorre qualquer erro na consulta do CEP.
    Returns:
        dict -- Dados do endereço do CEP consultado.
    """

    try:
        response = requests.get(URL_CEP_FROM_ADDRESS.format(state, city, street))  # noqa

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 400:
            raise exceptions.InvalidCityStateName('City and Street must be 3 characters of lenght')  # noqa
        else:
            raise exceptions.BaseException('Other error. Status code: %d' % response.status_code)  # noqa

    except requests.exceptions.ConnectionError as errc:
        raise exceptions.ConnectionError(errc)

    except requests.exceptions.Timeout as errt:
        raise exceptions.Timeout(errt)

    except requests.exceptions.HTTPError as errh:
        raise exceptions.HTTPError(errh)

    except requests.exceptions.RequestException as e:
        raise exceptions.BaseException(e)
