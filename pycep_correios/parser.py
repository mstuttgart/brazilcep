# -*- encoding: utf8 -*-

import xml.etree.cElementTree as Et
from jinja2 import Environment, PackageLoader


def parse_response(xml):

    end = Et.fromstring(xml).find('.//return')

    address = {
        'logradouro': end.findtext('end'),
        'bairro': end.findtext('bairro'),
        'cidade': end.findtext('cidade'),
        'uf': end.findtext('uf'),
        'complemento': end.findtext('complemento'),
        'outro': end.findtext('complemento2')
    }

    return address


def parse_error_response(xml):
    return Et.fromstring(xml).findtext('.//faultstring')


def mount_request(cep):
    env = Environment(loader=PackageLoader('pycep_correios', 'templates'))
    template = env.get_template('consultacep.xml')
    xml = template.render(cep=cep)
    return (xml.replace('\n', '')).replace('\t', '')
