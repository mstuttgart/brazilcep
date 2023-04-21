"""
brazilcep.exceptions
~~~~~~~~~~~~~~~~~~~~

This module implements the BrazilCEP exceptions.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""


class BrazilCEPException(Exception):
    """Base class for exceptions"""


class InvalidCEP(BrazilCEPException):
    """Exception raised to invalid CEP requests"""


class CEPNotFound(BrazilCEPException):
    """Exception raised to CEP not founded requests"""


class BlockedByFlood(BrazilCEPException):
    """Exception raised by flood of requests"""
