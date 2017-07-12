# -*- coding: utf-8 -*-

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

from .cliente import consultar_cep, formatar_cep, validar_cep
from .cliente import HOMOLOGACAO, PRODUCAO
from .excecoes import CEPInvalido

__all__ = [
    'consultar_cep',
    'formatar_cep',
    'validar_cep',
    'CEPInvalido',
    'HOMOLOGACAO',
    'PRODUCAO',
]
