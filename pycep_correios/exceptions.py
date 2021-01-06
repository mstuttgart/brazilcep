
class BaseException(Exception):
    """Base class for exceptions"""


class InvalidCEP(BaseException):
    """Exception raised to invalid CEP requests"""


class CEPNotFound(BaseException):
    """Exception raised to CEP not founded requests"""


class ConnectionError(BaseException):
    """Exception raised to requests with connection errors"""


class HTTPError(BaseException):
    """Exception raised to requests with HTTPS errors"""


class Timeout(BaseException):
    """Exception raised to requests with timeout"""
