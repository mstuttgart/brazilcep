# -*- encoding: utf8 -*-

import xml.etree.cElementTree as Et


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
