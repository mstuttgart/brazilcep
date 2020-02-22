from .client import (HOMOLOGACAO, PRODUCAO, consultar_cep, format_cep,  # noqa
                     formatar_cep, get_address_from_cep, get_cep_from_address,
                     validar_cep, validate_cep)
from .excecoes import CEPInvalido
from .exceptions import BaseException

__all__ = [
    'consultar_cep',
    'formatar_cep',
    'validar_cep',
    'get_address_from_cep',
    'get_cep_from_address',
    'format_cep',
    'validate_cep',
    'CEPInvalido',
    'BaseException',
    'HOMOLOGACAO',
    'PRODUCAO',
]
