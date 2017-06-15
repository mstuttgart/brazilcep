# -*- coding: utf-8 -*-

__title__ = 'PyCEP Correios'
__version__ = '1.1.7'
__author__ = 'Michell Stuttgart Faria'
__maintainer__ = 'Michell Stuttgart Faria'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015-2017 Michell Stuttgart Faria'
__status__ = 'Production'

__all__ = [
    'consultar_cep',
    'formatar_cep',
    'validar_cep',
    'CEPInvalido',
]

from .cliente import consultar_cep, formatar_cep, validar_cep
from .excecoes import CEPInvalido
