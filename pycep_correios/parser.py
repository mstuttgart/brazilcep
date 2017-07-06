# -*- encoding: utf8 -*-

from __future__ import absolute_import, unicode_literals

import xml.etree.cElementTree as Et

import jinja2
import six


def parse_resposta(xml):
    """Extrai os endereço do xml retornado pelo webservice

    :param xml: xml retornado pelo webservice
    :type xml: str
    :return: dados do endereço do CEP consultado
    :rtype: dict
    """

    if isinstance(xml, six.string_types):
        xml = xml.encode('utf8')
    else:
        xml = xml.decode('utf8')

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
    :return: string contendo mensagem de erro
    :rtype: str
    """
    if isinstance(xml, six.string_types):
        xml = xml.encode('utf8')
    else:
        xml = xml.decode('utf8')

    return Et.fromstring(xml).findtext('.//faultstring')


def monta_requisicao(cep):
    """Gera o XML utilizado para realizar a requisição ao webservice

    :param cep: CEP a ser consultado
    :type cep: str
    :return: XML de consulta com CEP fornecido
    :rtype: str
    """
    loader = jinja2.PackageLoader('pycep_correios', 'templates')
    env = jinja2.Environment(loader=loader)
    template = env.get_template('consultacep.xml')
    xml = template.render(cep=cep)
    return (xml.replace('\n', '')).replace('\t', '')
