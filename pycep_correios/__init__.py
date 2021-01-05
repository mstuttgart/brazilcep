from .client import WebService, get_address_from_cep, get_cep_from_address  # noqa
from .exceptions import BaseException

__all__ = [
    'get_address_from_cep',
    'get_cep_from_address',
    'BaseException',
    'WebService',
]
