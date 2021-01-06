import json

import requests

from . import exceptions

URL = 'https://ws.apicep.com/cep/{}.json'


def fetch_address(cep):

    try:
        response = requests.get(URL.format(cep))

        if response.status_code == 200:

            # Transforma o objeto requests em um dict
            address = json.loads(response.text)

            if address['status'] == 400:
                raise exceptions.InvalidCEP()

            if address['status'] == 404:
                raise exceptions.CEPNotFound()

            return {
                'bairro': address.get('district', ''),
                'cep': address.get('code', ''),
                'cidade': address.get('city', ''),
                'logradouro': address.get('address', '').split(' - até')[0],
                'uf': address.get('state', ''),
                'complemento': '',
            }

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
