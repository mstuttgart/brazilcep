"""
brazilcep.exceptions
~~~~~~~~~~~~~~~~~~~~

This module defines custom exceptions used in the BrazilCEP library.

These exceptions are designed to handle various error scenarios that may occur
when interacting with the BrazilCEP library, such as invalid input, connection
issues, or HTTP-related errors.

Classes:
    - BrazilCEPException: Base class for all exceptions in the BrazilCEP library.
    - InvalidCEP: Raised when an invalid CEP (postal code) is provided.
    - CEPNotFound: Raised when a requested CEP cannot be found.
    - BlockedByFlood: Raised when requests are blocked due to excessive traffic.
    - ConnectionError: Raised when a connection error occurs.
    - HTTPError: Raised when an HTTP error is encountered.
    - URLRequired: Raised when an invalid or missing URL is used for a request.
    - TooManyRedirects: Raised when too many redirects occur during a request.
    - Timeout: Raised when a request exceeds the allowed time limit.
    - JSONLoadError: Raised when a JSON parsing operation fails.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""


class BrazilCEPException(Exception):
    """
    Base class for exceptions
    """


class InvalidCEP(BrazilCEPException):
    """
    Exception raised for invalid CEP requests
    """


class CEPNotFound(BrazilCEPException):
    """
    Exception raised when a CEP is not found
    """


class BlockedByFlood(BrazilCEPException):
    """
    Exception raised due to a flood of requests being blocked
    """


class ConnectionError(BrazilCEPException):
    """
    Exception raised by a BrazilCEP connection error
    """


class HTTPError(BrazilCEPException):
    """
    Exception raised by HTTP error
    """


class URLRequired(BrazilCEPException):
    """
    Exception raised for using an invalid URL to make a request
    """


class TooManyRedirects(BrazilCEPException):
    """
    Exception raised by too many redirects
    """


class Timeout(BrazilCEPException):
    """
    Exception raised when a request times out
    """


class JSONLoadError(BrazilCEPException):
    """
    Exception raised when a JSON loading operation fails
    """
