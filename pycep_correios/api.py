# -*- coding: utf-8 -*-

import requests

from .excecoes import CEPInvalido
from .parser import parse_resposta_com_erro, parse_resposta, monta_requisicao

URL = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/' \
      'AtendeCliente?wsdl'


def consultar_cep(cep):
    """Retorna o endereço correspondente ao número de CEP informado.

    :param cep: CEP a ser consultado.
    :type cep: str
    :returns: Dados do endereço do cep consultado.
    :rtype: dict
    :raises :exc:`CEPInvalido`: Exceção para CEP inválido
    """

    xml = monta_requisicao(formatar_cep(cep))

    header = {'Content-type': 'text/xml; charset=;%s' % 'utf8'}

    try:
        resposta = requests.post(URL, data=xml, headers=header, verify=False)
    except requests.exceptions.RequestException as e:
        raise e
    else:
        if resposta.ok:
            return parse_resposta(resposta.text)
        else:
            msg = parse_resposta_com_erro(resposta.text)
            raise CEPInvalido(msg)


def formatar_cep(cep):
    """Formata CEP, removendo pontos e hiphens

    :param cep: CEP to be format
    :type cep: str
    :returns: Address data from CEP
    :rtype: str
    """
    cep = cep.replace('-', '')
    cep = cep.replace('.', '')
    return cep


def validar_cep(cep):
    """Verifica se o CEP informado possui 8 digitos e é constituído apenas de
    números

    :param cep: CEP a ser validado
    :type cep: str
    :returns: se o CEP informado é valido
    :rtype: boolean
    """
    cep = formatar_cep(cep)
    return cep.isdigit() and len(cep) == 8
