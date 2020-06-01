
"""
pycep_correios.client
~~~~~~~~~~~~~~~~~~~~~
Este modulo implementa o cliente para consulta de CEP da PyCEPCorreios.

:copyright: 2016-2020 por Michell Stuttgart Faria
:license: MIT, veja o arquivo LICENSE para mais detalhes.

"""
import json
import logging
import re
import warnings

import deprecated
import requests
import zeep
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from . import excecoes, exceptions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CARACTERES_NUMERICOS = re.compile(r'[^0-9]')
NUMBERS = re.compile(r'[^0-9]')

PRODUCAO = 1
HOMOLOGACAO = 2

URL = {
    HOMOLOGACAO: 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  # noqa: E501
    PRODUCAO: 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  # noqa: E501
}

URL_GET_ADDRESS_FROM_CEP = 'http://www.viacep.com.br/ws/{}/json'
URL_GET_CEP_FROM_ADDRESS = 'http://www.viacep.com.br/ws/{}/{}/{}/json'


@deprecated.deprecated(version='4.0.0', reason="'consultar_cep' is no longer supported and will be removed in a future release. Please, use 'get_address_from_cep' instead.")
def consultar_cep(cep, ambiente=PRODUCAO):
    """Retorna o endereço correspondente ao número de CEP informado.

    Arguments:
        cep {str} -- CEP a ser consultado.

    Keyword Arguments:
        ambiente {int} -- Indica qual será o webservice utilizado na consulta de CEP. Valor default é PRODUCAO (default: {PRODUCAO})

    Raises:
        KeyError -- Quando ambiente selecionado não existe (esperado: PRODUCAO ou HOMOLOGACAO)
        ExcecaoPyCEPCorreios -- Quando ocorre qualquer erro na consulta do CEP.

    Returns:
        dict -- Dados do endereço do CEP consultado.
    """

    if ambiente not in URL:
        raise KeyError('Ambiente inválido! Valor deve ser 1 para produção e 2 '
                       'para homologação')

    try:
        with warnings.catch_warnings():
            # Desabilitamos o warning
            warnings.simplefilter('ignore', InsecureRequestWarning)
            warnings.simplefilter('ignore', ImportWarning)
            client = zeep.Client(URL[ambiente])
            endereco = client.service.consultaCEP(formatar_cep(cep))

            return {
                'bairro': getattr(endereco, 'bairro', ''),
                'cep': getattr(endereco, 'cep', ''),
                'cidade': getattr(endereco, 'cidade', ''),
                'end': getattr(endereco, 'end', ''),
                'uf': getattr(endereco, 'uf', ''),
                'complemento2': getattr(endereco, 'complemento2', ''),
                'unidadesPostagem': getattr(endereco, 'unidadesPostagem', []),
            }

    except zeep.exceptions.Fault as e:
        raise excecoes.ExcecaoPyCEPCorreios(message=e.message)


@deprecated.deprecated(version='4.0.0', reason="'formatar_cep' is no longer supported and will be removed in a future release. Please, use 'format_cep' instead.")
def formatar_cep(cep):
    """Formata CEP, removendo qualquer caractere não numérico.

    Arguments:
        cep {str} -- CEP a ser formatado.

    Raises:
        ValueError -- Quando a string esta vazia ou não contem numeros.

    Returns:
        str -- string contendo o CEP formatado.
    """
    if not isinstance(cep, str) or not cep:
        raise ValueError('CEP deve ser uma string não vazia '
                         'contendo somente numeros')

    return CARACTERES_NUMERICOS.sub('', cep)


@deprecated.deprecated(version='4.0.0', reason="'validar_cep' is no longer supported and will be removed in a future release. Please, use 'validate_cep' instead.")
def validar_cep(cep):
    """Verifica se o CEP informado possui 8 digitos e é constituído apenas de números.

    Arguments:
        cep {str} -- CEP a ser validado.

    Returns:
        [boolean] -- True se o CEP informado é valido. Caso contrário, retorna False.
    """
    cep = formatar_cep(cep)
    return cep.isdigit() and len(cep) == 8


def get_address_from_cep(cep):
    """Retorna o endereço correspondente ao número de CEP informado.

    Arguments:
        cep {str} -- CEP a ser consultado.
    Raises:
        BaseException -- Quando ocorre qualquer erro na consulta do CEP.
    Returns:
        dict -- Dados do endereço do CEP consultado.
    """

    cep = format_cep(cep)

    try:
        response = requests.get(URL_GET_ADDRESS_FROM_CEP.format(cep))

        if response.status_code == 200:
            address = json.loads(response.text)

            if 'error' in address and address['error']:
                raise exceptions.BaseException(message='Other error')

            return {
                'bairro': address.get('bairro', ''),
                'cep': address.get('cep', ''),
                'cidade': address.get('localidade', ''),
                'logradouro': address.get('logradouro', ''),
                'uf': address.get('uf', ''),
                'complemento': address.get('complemento', ''),
            }

        elif response.status_code == 400:
            raise exceptions.BaseException(message='Invalid CEP: %s' % cep)  # noqa
        else:
            raise exceptions.BaseException(message='Other error')

    except requests.exceptions.RequestException as e:
        raise exceptions.BaseException(message=e.message)


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
