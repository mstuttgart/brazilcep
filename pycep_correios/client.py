import enum
import re

from . import apicep, correios, viacep

NUMBERS = re.compile(r'[^0-9]')


class WebService(enum.Enum):
    CORREIOS = 0
    VIACEP = 1
    APICEP = 2


def get_address_from_cep(cep, webservice=WebService.APICEP):
    """Retorna o endereço correspondente ao número de CEP informado.

    Arguments:
        cep {str} -- CEP a ser consultado.
    Raises:
        BaseException -- Quando ocorre qualquer erro na consulta do CEP.
    Returns:
        dict -- Dados do endereço do CEP consultado.
    """

    if webservice not in (value for attribute, value in WebService.__dict__.items()):  # noqa
        raise KeyError("""Invalid webservice. Please use this options:
        WebService.CORREIOS, WebService.VIACEP, WebService.APICEP
    """)

    cep = _format_cep(cep)

    if webservice == WebService.CORREIOS:
        return correios.fetch_address(cep)

    if webservice == WebService.VIACEP:
        return viacep.fetch_address(cep)

    if webservice == WebService.APICEP:
        return apicep.fetch_address(cep)


def _format_cep(cep):
    """Formata CEP, removendo qualquer caractere não numérico.

    Arguments:
        cep {str} -- CEP a ser formatado.
    Raises:
        ValueError -- Quando a string esta vazia ou não contem numeros.
    Returns:
        str -- string contendo o CEP formatado.
    """
    if not isinstance(cep, str) or not cep:
        raise ValueError('CEP must be a non-empty string containing only numbers')  # noqa

    return NUMBERS.sub('', cep)
