# -*- encoding: utf8 -*-

import xml.etree.cElementTree as Et
from jinja2 import Environment, PackageLoader


def parse_resposta(xml):
    """Extrai os endereço do xml retornado pelo webservice

    :param xml: xml retornado pelo webservice
    :type xml: str
    :returns endereco: dados do endereço do CEP consultado
    :rtype: dict
    """

    end = Et.fromstring(xml).find('.//return')

    endereco = {
        'id': end.findtext('id'),
        'end': end.findtext('end'),
        'cep': end.findtext('cep'),
        'bairro': end.findtext('bairro'),
        'cidade': end.findtext('cidade'),
        'uf': end.findtext('uf'),
        'complemento': end.findtext('complemento'),
        'complemento2': end.findtext('complemento2'),
    }

    return endereco


def parse_resposta_com_erro(xml):
    """Realiza a leitura do XML retornado pelo servidor e extrai a mensagem de
    erro

    :param xml: XML retornado pelo webservice
    :type xml: str
    :returns: mensagem de erro
    :rtype: str
    """
    return Et.fromstring(xml).findtext('.//faultstring')


def monta_requisicao(cep):
    """Gera o XML utilizado para realizar a requesição ao webservice

    :param cep: CEP a ser consultado
    :type xml: str
    :returns: XML de consulta contendo o CEP fornecido
    :rtype: str
    """
    env = Environment(loader=PackageLoader('pycep_correios', 'templates'))
    template = env.get_template('consultacep.xml')
    xml = template.render(cep=cep)
    return (xml.replace('\n', '')).replace('\t', '')
