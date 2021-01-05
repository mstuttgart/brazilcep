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

    if webservice not in (value for attribute, value in WebService.__dict__.items()):
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

    #     try:
    #         with warnings.catch_warnings():
    #             # Desabilitamos o warning
    #             warnings.simplefilter('ignore', InsecureRequestWarning)
    #             warnings.simplefilter('ignore', ImportWarning)

    #             client = zeep.Client(webservice)

    #             address = client.service.consultaCEP(cep)

    #             return {
    #                 'bairro': getattr(address, 'bairro', ''),
    #                 'cep': getattr(address, 'cep', ''),
    #                 'cidade': getattr(address, 'cidade', ''),
    #                 'logradouro': getattr(address, 'end', ''),
    #                 'uf': getattr(address, 'uf', ''),
    #                 'complemento': getattr(address, 'complemento2', ''),
    #             }

    #     except zeep.exceptions.Fault as e:
    #         raise exceptions.BaseException(message=e)

    # else:

    #     try:
    #         response = requests.get(webservice.format(cep))

    #         if response.status_code == 200:

    #             address = json.loads(response.text)

    #             if address.get('erro'):
    #                 raise exceptions.BaseException(message='Other error. Status code: %d' % response.status_code)  # noqa

    #             return {
    #                 'bairro': address.get('bairro', '') or address.get('district', ''),
    #                 'cep': address.get('cep', '') or address.get('code', ''),
    #                 'cidade': address.get('localidade', '') or address.get('city', ''),
    #                 'logradouro': address.get('logradouro', '') or address.get('address', '').split(' - até')[0],
    #                 'uf': address.get('uf', '') or address.get('state', ''),
    #                 'complemento': address.get('complemento', ''),
    #             }

    #         elif response.status_code == 400:
    #             raise exceptions.BaseException(message='Invalid CEP: %s' % cep)  # noqa

    #         elif response.status_code == 404:
    #             raise exceptions.BaseException(message='CEP not found: %s' % cep)  # noqa

    #         else:
    #             raise exceptions.BaseException(
    #                 message='Other error. Status code: %d' % response.status_code)

    #     except requests.exceptions.RequestException as e:
    #         raise exceptions.BaseException(message=e)


def get_cep_from_address(state, city, street):
    """Retorna os CEPs correspondente ao endereço informado.

    Arguments:
        state {str} -- Sigla do estado da consulta
        city {str} -- Cidade do CEP ser encontrado
        street {str} -- Rua do CEP a ser encontrado
    Raises:
        BaseException -- Quando ocorre qualquer erro na consulta do CEP.
    Returns:
        dict -- Dados do endereço do CEP consultado.
    """

    return viacep.fetch_cep(state=state, city=city, street=street)

    # try:
    #     response = requests.get(URL_GET_CEP_FROM_ADDRESS.format(state, city, street))  # noqa

    #     if response.status_code == 200:
    #         return response.json()

    #     elif response.status_code == 400:
    #         raise exceptions.BaseException('City and Street must be 3 characters of lenght')  # noqa
    #     else:
    #         raise exceptions.BaseException('Other error ocurred!')

    # except requests.exceptions.RequestException as e:
    #     raise exceptions.BaseException(e)


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
