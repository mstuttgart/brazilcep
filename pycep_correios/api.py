# -*- coding: utf-8 -*-

import requests

from .exceptions import ConnectionError, InvalidCEP, TimeOut, TooManyRedirects
from .parser import parse_error_response, parse_response, mount_request

URL = 'https://apps.correios.com.br/SigepMasterJPA' \
          '/AtendeClienteService/AtendeCliente?wsdl'


def get_address(cep):
    """Return address (logradouro, bairro, cidade, estado) from CEP code

    :param cep: CEP a ser consultado.
    :type cep: str
    :returns: Dados do endereço do cep consultado.
    :rtype: dict
    :raises: :exc:`ExceptionType`
    :raises :exc:`TimeOut`: connection timout exception
    :raises :exc:`TooManyRedirects`: many redirections exception
    :raises :exc:`ConnectionError`: connection exception
    :raises :exc:`InvalidCEP`: invalid cep exception
    """

    xml = mount_request(format_cep(cep))

    header = {'Content-type': 'text/xml; charset=;%s' % 'utf8'}

    try:
        response = requests.post(URL,
                                 data=xml,
                                 headers=header,
                                 verify=False)

    except requests.exceptions.Timeout:
        msg = 'Tempo de conexão excedido. Por favor, tente mais tarde.'
        raise TimeOut(msg)

    except requests.exceptions.TooManyRedirects:
        msg = 'Formato de requisição inválido. Por favor, verifique sua ' \
              'requisição etente novamente'
        raise TooManyRedirects(msg)

    except requests.ConnectionError:
        msg = 'Erro ao conectar a API. Por favor, verifique sua conexão.'
        raise ConnectionError(msg)
    else:

        if not response.ok:
            msg = parse_error_response(response.text)
            raise InvalidCEP(msg)

        return parse_response(response.text)


def format_cep(cep):
    """Return cep code with digits
    :param cep: CEP a ser formatado
    :type cep: str
    :returns: Dados do endereço do cep consultado
    :rtype: str
    """
    cep = cep.replace('-', '')
    cep = cep.replace('.', '')
    return cep


def validate_cep(cep):
    """
    """
    cep = format_cep(cep)
    return cep.isdigit() and len(cep) == 8
