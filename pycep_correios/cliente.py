# -*- coding: utf-8 -*-

"""
pycep_correios.client
~~~~~~~~~~~~~~~~~~~~~
Este modulo implementa o cliente para consulta de CEP da PyCEPCorreios.

:copyright: 2016-2017 por Michell Stuttgart Faria
:license: MIT, veja o arquivo LICENSE para mais detalhes.

"""

from __future__ import absolute_import, unicode_literals

import re

import requests
import six

from . import excecoes, parser

CARACTERES_NUMERICOS = re.compile(r'[^0-9]')

PRODUCAO = 1
HOMOLOGACAO = 2

URL = {
    HOMOLOGACAO: 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  # noqa: E501
    PRODUCAO: 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  # noqa: E501
}


def consultar_cep(cep, ambiente=PRODUCAO):
    """Retorna o endereço correspondente ao número de CEP informado.

    :param cep: CEP a ser consultado.
    :type cep: str
    :param ambiente: Indica qual será o webservice utilizado na consulta de CEP. Valor default é PRODUCAO. # noqa: E501
    :type ambiente: int
    :return: Dados do endereço do CEP consultado.
    :rtype: dict
    :raises CEPInvalido: quando a cep é inexistente
    """

    if ambiente not in URL:
        raise KeyError('Ambiente inválido! Valor deve ser 1 para produção e 2 '
                       'para homologação')

    xml = parser.monta_requisicao(formatar_cep(cep))

    header = {'Content-type': 'text/xml; charset=;%s' % 'utf8'}

    try:
        resposta = requests.post(URL[ambiente],
                                 data=xml,
                                 headers=header,
                                 verify=False)

    except requests.ConnectTimeout as exc:
        msg = 'Mensagem original: %s' % exc
        raise excecoes.Timeout('Timout! Conexão excedeu limite de tempo! '
                               '%s' % msg)

    except requests.ConnectionError as exc:
        msg = 'Mensagem original: %s' % exc
        raise excecoes.FalhaNaConexao('Falha na Conexão! %s' % msg)

    except requests.TooManyRedirects as exc:
        msg = 'Mensagem original: %s' % exc
        raise excecoes.MultiploRedirecionamento('Multiplos redirecionamentos '
                                                'durante a conexão! %s' % msg)

    except requests.RequestException as exc:
        msg = 'Mensagem original: %s' % exc
        raise excecoes.ExcecaoPyCEPCorreios('Uma excecao inesperada '
                                            'ocorreu: %s' % msg)

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
        raise ValueError('CEP deve ser uma string não vazia '
                         'contendo somente numeros')

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
