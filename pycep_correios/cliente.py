# -*- coding: utf-8 -*-

import requests

from .excecoes import CEPInvalido
from .parser import parse_resposta_com_erro, parse_resposta, monta_requisicao

URL = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/' \
      'AtendeCliente?wsdl'


def consultar_cep(cep: str) -> dict:
    """Retorna o endereço correspondente ao número de CEP informado.

    :param cep: CEP a ser consultado.
    :returns: Dict com os dados do endereço do CEP consultado.
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


def formatar_cep(cep: str) -> str:
    """Formata CEP, removendo pontuação

    :param cep: CEP a ser formatado
    :returns: string contendo o CEP formatado
    """
    cep = cep.replace('-', '')
    cep = cep.replace('.', '')
    return cep


def validar_cep(cep: str) -> bool:
    """Verifica se o CEP informado possui 8 digitos e é constituído apenas de
    números

    :param cep: CEP a ser validado
    :returns: True se o CEP informado é valido. Caso contrário, retorna False
    """
    cep = formatar_cep(cep)
    return cep.isdigit() and len(cep) == 8
