"""
BrazilCEP
~~~~~~~~~

BrazilCEP is a minimalist and easy-to-use python library designed to query
CEP (brazilian zip codes) data.

Its objective is to provide a common query interface to all these search services,
facilitating the integration of Python applications with these services.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

from .client import WebService, get_address_from_cep

__all__ = [
    "get_address_from_cep",
    "WebService",
]
