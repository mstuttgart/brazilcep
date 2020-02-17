
class BaseException(Exception):
    """ base exception"""

    def __init__(self, message=''):
        super(BaseException, self).__init__(message)
        self.message = message

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.message)
