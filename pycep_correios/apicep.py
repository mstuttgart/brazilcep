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

            if address['status'] == 400 and address['message'] == "CEP informado é inválido":
                raise exceptions.InvalidCEP()

            if address['status'] == 400 and address['message'] == "Blocked by flood":
                raise exceptions.BlockedByFlood()

            if address['status'] == 404:
                raise exceptions.CEPNotFound()

            return {
                'bairro': address.get('district') or '',
                'cep': address.get('code') or '',
                'cidade': address.get('city') or '',
                'logradouro': (address.get('address') or '').split(' - até')[0],
                'uf': address.get('state') or '',
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
