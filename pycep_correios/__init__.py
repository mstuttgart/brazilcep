from .__version__ import (__title__,  # noqa: F401
                          __description__,
                          __version__,
                          __author__,
                          __author_email__,
                          __maintainer__,
                          __maintainer_email__,
                          __url__,
                          __download_url__,
                          __copyright__,
                          __license__)

from .client import consultar_cep, formatar_cep, validar_cep
from .client import get_address_from_cep, get_cep_from_address, format_cep, validate_cep  # noqa
from .client import HOMOLOGACAO, PRODUCAO
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
