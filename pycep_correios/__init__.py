# -*- coding: utf-8 -*-

__title__ = 'PyCEP Correios'
__version__ = '1.1.7'
__author__ = 'Michell Stuttgart Faria'
__maintainer__ = 'Michell Stuttgart Faria'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015-2017 Michell Stuttgart Faria'
__status__ = 'Production'

from .api import get_address, format_cep

from .exceptions import (
    CorreiosCEPException, ConnectionError, TooManyRedirects, TimeOut,
    InvalidCEP
)
