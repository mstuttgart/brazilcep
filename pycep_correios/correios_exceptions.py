# -*- coding: utf-8 -*-


class CorreiosCEPException(Exception):
    """ Base class for other exceptions """
    pass


class CorreiosCEPConnectionErrorException(CorreiosCEPException):
    """ Connection error exception """
    pass


class CorreiosCEPTooManyRedirectsException(CorreiosCEPException):
    """ Many redirects exception """
    pass


class CorreiosTimeOutException(CorreiosCEPException):
    """ TimeOut exception """
    pass


class CorreiosCEPInvalidCEPException(CorreiosCEPException):
    """ Invalid CEP Exception. Raised when cep have incorrect
    length or not exist """
    pass
