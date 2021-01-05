
"""
pycep_correios.client
~~~~~~~~~~~~~~~~~~~~~
Este modulo implementa o cliente para consulta de CEP da PyCEPCorreios.

:copyright: 2016-2020 por Michell Stuttgart Faria
:license: MIT, veja o arquivo LICENSE para mais detalhes.

"""
import json
import re
import warnings

import requests
import zeep
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from . import exceptions

NUMBERS = re.compile(r'[^0-9]')

CORREIOS = 0
VIACEP = 1
APICEP = 2

URL_GET_ADDRESS_FROM_CEP = {
    VIACEP: 'http://www.viacep.com.br/ws/{}/json',
    APICEP: 'https://ws.apicep.com/cep/{}.json',
    CORREIOS: 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  # noqa
}

URL_GET_CEP_FROM_ADDRESS = 'http://www.viacep.com.br/ws/{}/{}/{}/json'

def get_address_from_cep(cep, server=APICEP):
    """Retorna o endereço correspondente ao número de CEP informado.

    Arguments:
        cep {str} -- CEP a ser consultado.
    Raises:
        BaseException -- Quando ocorre qualquer erro na consulta do CEP.
    Returns:
        dict -- Dados do endereço do CEP consultado.
    """

    if server not in URL_GET_ADDRESS_FROM_CEP:
        raise KeyError("""Invalid server. Please use this options: 
        from pycep_correios import CORREIOS, VIACEP, APICEP
    """)

    cep = format_cep(cep)

    if server == CORREIOS:

        try:
            with warnings.catch_warnings():
                # Desabilitamos o warning
                warnings.simplefilter('ignore', InsecureRequestWarning)
                warnings.simplefilter('ignore', ImportWarning)

                client = zeep.Client(URL_GET_ADDRESS_FROM_CEP[CORREIOS])

                address = client.service.consultaCEP(cep)

                return {
                    'bairro': getattr(address, 'bairro', ''),
                    'cep': getattr(address, 'cep', ''),
                    'cidade': getattr(address, 'cidade', ''),
                    'logradouro': getattr(address, 'end', ''),
                    'uf': getattr(address, 'uf', ''),
                    'complemento': getattr(address, 'complemento2', ''),
                }

        except zeep.exceptions.Fault as e:
            raise exceptions.BaseException(message=e)

    try:
        response = requests.get(URL_GET_ADDRESS_FROM_CEP[server].format(cep))

        if response.status_code == 200:
            address = json.loads(response.text)

            if address.get('erro'):
                raise exceptions.BaseException(message='Other error')

            return {
                'bairro': address.get('bairro', '') or address.get('district', ''),
                'cep': address.get('cep', '') or address.get('code', ''),
                'cidade': address.get('localidade', '') or address.get('city', ''),
                'logradouro': address.get('logradouro', '') or address.get('address', '').split(' - até')[0],
                'uf': address.get('uf', '') or address.get('state', ''),
                'complemento': address.get('complemento', ''),
            }

        elif response.status_code == 400:
            raise exceptions.BaseException(message='Invalid CEP: %s' % cep)  # noqa
        else:
            raise exceptions.BaseException(message='Other error')

    except requests.exceptions.RequestException as e:
        raise exceptions.BaseException(message=e)


def get_cep_from_address(state, city, street):
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
        response = requests.get(
            URL_GET_CEP_FROM_ADDRESS.format(state, city, street))

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 400:
            raise exceptions.BaseException(
                message='City and Street must be 3 characters of lenght')
        else:
            raise exceptions.BaseException(
                message='Other error ocurred!')

    except requests.exceptions.RequestException as e:
        raise exceptions.BaseException(message=e.message)


def format_cep(cep):
    """Formata CEP, removendo qualquer caractere não numérico.

    Arguments:
        cep {str} -- CEP a ser formatado.
    Raises:
        ValueError -- Quando a string esta vazia ou não contem numeros.
    Returns:
        str -- string contendo o CEP formatado.
    """
    if not isinstance(cep, str) or not cep:
        raise ValueError(
            'CEP must be a non-empty string containing only numbers')

    return NUMBERS.sub('', cep)


def validate_cep(cep):
    """Verifica se o CEP informado possui 8 digitos e é constituído apenas de números.
    Arguments:
        cep {str} -- CEP a ser validado.
    Returns:
        [boolean] -- True se o CEP informado é valido. Caso contrário, retorna False.
    """
    cep = format_cep(cep)
    return cep.isdigit() and len(cep) == 8
