# -*- coding: utf-8 -*-


class ExcecaoPyCEPCorreios(Exception):
    """ Excecao base da lib"""


class CEPInvalido(ExcecaoPyCEPCorreios):
    """ Excecao disparada quando o CEP possui tamanho incorreto
    (diferente de 8) e/ou não existe"""


class FalhaNaConexao(ExcecaoPyCEPCorreios):
    """ Erro de conexao durante a requisicao """


class MultiploRedirecionamento(ExcecaoPyCEPCorreios):
    """ Excecao de multiplo redirecionamento """


class Timeout(ExcecaoPyCEPCorreios):
    """ Erro de TimeOut  """
