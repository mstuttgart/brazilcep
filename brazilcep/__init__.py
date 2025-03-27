"""
BrazilCEP
~~~~~~~~~

BrazilCEP is a lightweight and user-friendly Python library for querying
CEP (Brazilian postal codes) data.

The library provides a unified and consistent interface for accessing
multiple CEP lookup services, making it easier to integrate Python
applications with these services.

Features:
- Simple and intuitive API.
- Support for both synchronous and asynchronous queries.
- Compatible with multiple CEP web services.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

from .__version__ import __version__
from .client import WebService, async_get_address_from_cep, get_address_from_cep

__all__ = [
    "get_address_from_cep",
    "async_get_address_from_cep",
    "WebService",
    "__version__",
]
