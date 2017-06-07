# -*- coding: utf-8 -*-

import requests

from .exceptions import InvalidCEP
from .parser import parse_error_response, parse_response, mount_request

URL = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'


def get_address(cep):
    """Return address (logradouro, bairro, cidade, estado) from CEP code

    :param cep: CEP a ser consultado.
    :type cep: str
    :returns: Dados do endereço do cep consultado.
    :rtype: dict
    :raises :exc:`InvalidCEP`: invalid cep exception
    """

    xml = mount_request(cep)

    header = {'Content-type': 'text/xml; charset=;%s' % 'utf8'}

    response = requests.post(URL, data=xml, headers=header, verify=False)

    if response.ok:
        return parse_response(response.text)
    else:
        msg = parse_error_response(response.text)
        raise InvalidCEP(msg)


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
