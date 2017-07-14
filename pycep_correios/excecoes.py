# -*- coding: utf-8 -*-


class ExcecaoBase(Exception):
    """ Excecao base da lib"""

    def __init__(self, *args, **kwargs):
        self.msg = kwargs.pop('msg', None)
        super(ExcecaoBase, self).__init__(*args, **kwargs)


class CEPInvalido(ExcecaoBase):
    """ Excecao disparada quando o CEP possui tamanho incorreto
    (diferente de 8) e/ou não existe"""


class FalhaNaConexao(ExcecaoBase):
    """ Erro de conexao durante a requisicao """


class MultiploRedirecionamento(ExcecaoBase):
    """ Excecao de multiplo redirecionamento """


class Timeout(ExcecaoBase):
    """ Erro de TimeOut  """
