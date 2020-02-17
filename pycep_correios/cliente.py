
"""
pycep_correios.client
~~~~~~~~~~~~~~~~~~~~~
Este modulo implementa o cliente para consulta de CEP da PyCEPCorreios.

:copyright: 2016-2019 por Michell Stuttgart Faria
:license: MIT, veja o arquivo LICENSE para mais detalhes.

"""
import logging
import re
import warnings

import deprecation
import zeep
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from . import excecoes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CARACTERES_NUMERICOS = re.compile(r'[^0-9]')

PRODUCAO = 1
HOMOLOGACAO = 2

URL = {
    HOMOLOGACAO: 'https://apphom.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  # noqa: E501
    PRODUCAO: 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl',  # noqa: E501
}


@deprecation.deprecated(version='4.0.0', reason="'consultar_cep' is no longer supported and will be removed in a future release. Please use 'get_address_from_cep'")
def consultar_cep(cep, ambiente=PRODUCAO):
    """Retorna o endereço correspondente ao número de CEP informado.

    Arguments:
        cep {str} -- CEP a ser consultado.

    Keyword Arguments:
        ambiente {int} -- Indica qual será o webservice utilizado na consulta de CEP. Valor default é PRODUCAO (default: {PRODUCAO})

    Raises:
        KeyError -- Quando ambiente selecionado não existe (esperado: PRODUCAO ou HOMOLOGACAO)
        ExcecaoPyCEPCorreios -- Quando ocorre qualquer erro na consulta do CEP.

    Returns:
        dict -- Dados do endereço do CEP consultado.
    """

    if ambiente not in URL:
        raise KeyError('Ambiente inválido! Valor deve ser 1 para produção e 2 '
                       'para homologação')

    try:
        with warnings.catch_warnings():
            # Desabilitamos o warning
            warnings.simplefilter('ignore', InsecureRequestWarning)
            warnings.simplefilter('ignore', ImportWarning)
            client = zeep.Client(URL[ambiente])
            endereco = client.service.consultaCEP(formatar_cep(cep))

            return {
                'bairro': getattr(endereco, 'bairro', ''),
                'cep': getattr(endereco, 'cep', ''),
                'cidade': getattr(endereco, 'cidade', ''),
                'end': getattr(endereco, 'end', ''),
                'uf': getattr(endereco, 'uf', ''),
                'complemento2': getattr(endereco, 'complemento2', ''),
                'unidadesPostagem': getattr(endereco, 'unidadesPostagem', []),
            }

    except zeep.exceptions.Fault as e:
        raise excecoes.ExcecaoPyCEPCorreios(message=e.message)


def formatar_cep(cep):
    """Formata CEP, removendo qualquer caractere não numérico.

    Arguments:
        cep {str} -- CEP a ser formatado.

    Raises:
        ValueError -- Quando a string esta vazia ou não contem numeros.

    Returns:
        str -- string contendo o CEP formatado.
    """
    if not isinstance(cep, str) or not cep:
        raise ValueError('CEP deve ser uma string não vazia '
                         'contendo somente numeros')

    return CARACTERES_NUMERICOS.sub('', cep)


def validar_cep(cep):
    """Verifica se o CEP informado possui 8 digitos e é constituído apenas de números.

    Arguments:
        cep {str} -- CEP a ser validado.

    Returns:
        [boolean] -- True se o CEP informado é valido. Caso contrário, retorna False.
    """
    cep = formatar_cep(cep)
    return cep.isdigit() and len(cep) == 8
