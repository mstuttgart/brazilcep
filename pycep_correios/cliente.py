# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import re

import requests
import six

from . import excecoes, parser

CARACTERES_NUMERICOS = re.compile(r'[^0-9]')

URL = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/' \
      'AtendeCliente?wsdl'


def consultar_cep(cep):
    """Retorna o endereço correspondente ao número de CEP informado.

    :param cep: CEP a ser consultado.
    :type cep: str
    :return: Dados do endereço do CEP consultado.
    :rtype: dict
    :raises CEPInvalido: quando a cep é inexistente
    """

    xml = parser.monta_requisicao(formatar_cep(cep))

    header = {'Content-type': 'text/xml; charset=;%s' % 'utf8'}

    try:
        resposta = requests.post(URL, data=xml, headers=header, verify=False)
    except requests.exceptions.RequestException as exc:
        raise exc
    else:
        if resposta.ok:
            return parser.parse_resposta(resposta.text)
        else:
            msg = parser.parse_resposta_com_erro(resposta.text)
            raise excecoes.CEPInvalido(msg)


def formatar_cep(cep):
    """Formata CEP, removendo qualquer caractere nao numerico

    :param cep: CEP a ser formatado
    :type cep: str
    :return: string contendo o CEP formatado
    :rtype: str
    :raises ValueError: quando a string esta vazia ou não contem numeros
    """
    if not isinstance(cep, six.string_types) or not cep:
        raise ValueError('cep deve ser uma string nao vazia contendo somente numeros')  # noqa: E501
    return CARACTERES_NUMERICOS.sub('', cep)


def validar_cep(cep):
    """Verifica se o CEP informado possui 8 digitos e é constituído apenas de
    números

    :param cep: CEP a ser validado
    :type cep: str
    :return: True se o CEP informado é valido. Caso contrário, retorna False
    :rtype: str
    :raises ValueError: quando a string esta vazia ou não contem numeros
    """
    cep = formatar_cep(cep)
    return cep.isdigit() and len(cep) == 8
