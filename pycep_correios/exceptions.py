# -*- coding: utf-8 -*-


class CorreiosCEPException(Exception):
    """ Base class for other exceptions """
    pass


class ConnectionError(CorreiosCEPException):
    """ Connection error exception """
    pass


class TooManyRedirects(CorreiosCEPException):
    """ Many redirects exception """
    pass


class TimeOut(CorreiosCEPException):
    """ TimeOut exception """
    pass


class InvalidCEP(CorreiosCEPException):
    """ Invalid CEP Exception. Raised when cep have incorrect
    length or not exist """
    pass
