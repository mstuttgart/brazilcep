# -*- coding: utf-8 -*-

import requests
from jinja2 import Environment, PackageLoader

from .exceptions import ConnectionError, InvalidCEP, TimeOut, TooManyRedirects
from .parser import parse_error_response, parse_response

URL = 'https://apps.correios.com.br/SigepMasterJPA' \
          '/AtendeClienteService/AtendeCliente?wsdl'


def get_address(cep):
    """Retorna dos dados do endereço de um dado cep

    :param cep: CEP a ser consultado.
    :type cep: str
    :returns: Dados do endereço do cep consultado.
    :rtype: dict
    :raises CorreiosTimeOutException: connection timout exception
    :raises CorreiosCEPTooManyRedirectsException: many redirections exception
    :raises CorreiosCEPConnectionErrorException: connection exception
    :raises CorreiosCEPInvalidCEPException: invalid cep exception

    Usage::

    >>> import pycep_correios
    >>> cep = '70503130'
    >>> address = pycep_correios.get_cep(cep)

    """

    xml = _mount_request(format_cep(cep))

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
    """
    """

    try:
        cep = cep.replace('-', '')
        cep = cep.replace('.', '')

        if not cep.isdigit():
            msg = 'CEP deve ser formado por números!'
            raise InvalidCEP(msg)

        return cep
    except AttributeError:
        msg = 'CEP deve ser do tipo string, ' \
              'mas o tipo encontrado foi %s!' % type(cep)
        raise InvalidCEP(msg)


def _mount_request(cep):
    env = Environment(loader=PackageLoader('pycep_correios', 'templates'))
    template = env.get_template('consultacep.xml')
    xml = template.render(cep=cep)
    return (xml.replace('\n', '')).replace('\t', '')
