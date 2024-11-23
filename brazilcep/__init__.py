"""
BrazilCEP
~~~~~~~~~

BrazilCEP is a minimalist and easy-to-use python library designed to query
CEP (brazilian zip codes) data.

Its objective is to provide a common query interface to all these search services,
facilitating the integration of Python applications with these services.

:copyright: (c) 2024 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

from .__version__ import __version__
from .client import WebService, get_address_from_cep

__all__ = [
    "get_address_from_cep",
    "WebService",
    "__version__",
]
