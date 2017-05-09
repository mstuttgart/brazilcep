# -*- coding: utf-8 -*-

import requests
import xml.etree.cElementTree as Et
from jinja2 import Environment, PackageLoader

from .correios_exceptions import CorreiosCEPConnectionErrorException
from .correios_exceptions import CorreiosCEPInvalidCEPException
from .correios_exceptions import CorreiosTimeOutException
from .correios_exceptions import CorreiosCEPTooManyRedirectsException


class Correios:

    URL = 'https://apps.correios.com.br/SigepMasterJPA' \
              '/AtendeClienteService/AtendeCliente?wsdl'

    @staticmethod
    def get_cep(cep: str) -> dict:
        """
        Retorna dos dados do endereço de um dado cep, a saber:
        rua: logradouro do cep
        bairro: bairro do cep
        cidade: cidade do cep
        uf: Abreviacao do estado do cep
        complemento: informações adicionais sobre o cep
        outro: informações variadas sobre o cep como por exemplo o intervalo
        de numero de residência que o mesmo compreende.

        :param cep: string contendo o cep a ser consultado
        :return: dict contendo os dados do endereço do cep consultado.
        """

        xml = Correios._mount_request(Correios._format_cep(cep))

        try:
            response = requests.post(Correios.URL,
                                     data=xml,
                                     headers={
                                         'Content-type': 'text/xml',
                                     },
                                     verify=False)

        except requests.exceptions.Timeout:
            msg = 'Tempo de conexão excedido. Por favor, tente mais tarde.'
            raise CorreiosTimeOutException(msg)

        except requests.exceptions.TooManyRedirects:
            msg = 'Formato de requisição inválido. Por favor, verifique sua ' \
                  'requisição etente novamente'
            raise CorreiosCEPTooManyRedirectsException(msg)

        except requests.ConnectionError:
            msg = 'Erro ao conectar a API. Por favor, verifique sua conexão.'
            raise CorreiosCEPConnectionErrorException(msg)
        else:

            if not response.ok:

                msg = Correios._parse_error(response.text)
                raise CorreiosCEPInvalidCEPException(msg)

            return Correios._parse_response(response.text)

    @staticmethod
    def _format_cep(cep):

        try:
            cep = cep.replace('-', '')
            cep = cep.replace('.', '')

            if not cep.isdigit():
                msg = 'CEP deve ser formado por números!'
                raise CorreiosCEPInvalidCEPException(msg)

            return cep
        except AttributeError:
            msg = 'CEP deve ser do tipo string, ' \
                  'mas o tipo encontrado foi %s!' % type(cep)
            raise CorreiosCEPInvalidCEPException(msg)

    @staticmethod
    def _mount_request(cep):
        env = Environment(loader=PackageLoader('pycep_correios', 'templates'))
        template = env.get_template('consultacep.xml')
        xml = template.render(cep=cep)
        return (xml.replace('\n', '')).replace('\t', '')

    @staticmethod
    def _parse_response(xml):

        end = Et.fromstring(xml).find('.//return')

        address = {
            'rua': end.findtext('end'),
            'bairro': end.findtext('bairro'),
            'cidade': end.findtext('cidade'),
            'uf': end.findtext('uf'),
            'complemento': end.findtext('complemento'),
            'outro': end.findtext('complemento2')
        }

        return address

    @staticmethod
    def _parse_error(xml):
        return Et.fromstring(xml).findtext('.//faultstring')
