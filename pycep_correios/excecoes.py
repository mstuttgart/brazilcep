import deprecation

from .__version__ import __version__


class ExcecaoPyCEPCorreios(Exception):
    """ Excecao base da lib"""

    def __init__(self, message=''):
        super(ExcecaoPyCEPCorreios, self).__init__(message)
        self.message = message

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.message)


@deprecation.deprecated(deprecated_in='3.0.0',
                        removed_in='4.0.0',
                        current_version=__version__,
                        details='Utilize a ExcecaoPyCEPCorreios')
class CEPInvalido(ExcecaoPyCEPCorreios):
    """ Excecao disparada quando o CEP possui tamanho incorreto
    (diferente de 8) e/ou não existe"""


@deprecation.deprecated(deprecated_in='3.0.0',
                        removed_in='4.0.0',
                        current_version=__version__,
                        details='Utilize a ExcecaoPyCEPCorreios')
class FalhaNaConexao(ExcecaoPyCEPCorreios):
    """ Erro de conexao durante a requisicao """


@deprecation.deprecated(deprecated_in='3.0.0',
                        removed_in='4.0.0',
                        current_version=__version__,
                        details='Utilize a ExcecaoPyCEPCorreios')
class MultiploRedirecionamento(ExcecaoPyCEPCorreios):
    """ Excecao de multiplo redirecionamento """


@deprecation.deprecated(deprecated_in='3.0.0',
                        removed_in='4.0.0',
                        current_version=__version__,
                        details='Utilize a ExcecaoPyCEPCorreios')
class Timeout(ExcecaoPyCEPCorreios):
    """ Erro de TimeOut  """
