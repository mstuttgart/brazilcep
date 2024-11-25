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


class ConnectionError(BrazilCEPException):
    """Exception raised by a connection error"""


class HTTPError(BrazilCEPException):
    """Exception raised by HTTP error"""


class URLRequired(BrazilCEPException):
    """Exception raised by using a invalid URL to make a request"""


class TooManyRedirects(BrazilCEPException):
    """Exception raised by too many redirects"""


class Timeout(BrazilCEPException):
    """Exception raised by request timed out"""
