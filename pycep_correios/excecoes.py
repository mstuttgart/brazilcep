import deprecated


@deprecated.deprecated(version='4.0.0', reason="Please, use 'BaseException' instead")
class ExcecaoPyCEPCorreios(Exception):
    """ Excecao base da lib"""

    def __init__(self, message=''):
        super(ExcecaoPyCEPCorreios, self).__init__(message)
        self.message = message

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.message)


@deprecated.deprecated(version='4.0.0', reason="Please, use 'BaseException' instead")
class CEPInvalido(ExcecaoPyCEPCorreios):
    """ Excecao disparada quando o CEP possui tamanho incorreto
    (diferente de 8) e/ou não existe"""


@deprecated.deprecated(version='4.0.0', reason="Please, use 'BaseException' instead")
class FalhaNaConexao(ExcecaoPyCEPCorreios):
    """ Erro de conexao durante a requisicao """


@deprecated.deprecated(version='4.0.0', reason="Please, use 'BaseException' instead")
class MultiploRedirecionamento(ExcecaoPyCEPCorreios):
    """ Excecao de multiplo redirecionamento """


@deprecated.deprecated(version='4.0.0', reason="Please, use 'BaseException' instead")
class Timeout(ExcecaoPyCEPCorreios):
    """ Erro de TimeOut  """
