import json

import requests

from . import exceptions

URL = 'http://www.viacep.com.br/ws/{}/json'


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
