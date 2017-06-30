# -*- encoding: utf8 -*-

import xml.etree.cElementTree as Et
from jinja2 import Environment, PackageLoader


def parse_resposta(xml):
    """Extrai os endereço do xml retornado pelo webservice

    :param xml: xml retornado pelo webservice
    :returns endereco: dict com os dados do endereço do CEP consultado
    """

    if isinstance(xml, bytes):
        xml = xml.decode('utf8')
    else:
        xml = xml.encode('utf8')

    end = Et.fromstring(xml).find(u'.//return')

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
    :returns: string contendo mensagem de erro
    """
    if isinstance(xml, str):
        xml = xml.encode('utf8')
    else:
        xml = xml.decode('utf8')

    return Et.fromstring(xml).findtext(u'.//faultstring')


def monta_requisicao(cep):
    """Gera o XML utilizado para realizar a requisição ao webservice

    :param cep: CEP a ser consultado
    :returns: string contendo o XML de consulta com CEP fornecido
    """
    env = Environment(loader=PackageLoader('pycep_correios', 'templates'))
    template = env.get_template('consultacep.xml')
    xml = template.render(cep=cep)
    return (xml.replace('\n', '')).replace('\t', '')
