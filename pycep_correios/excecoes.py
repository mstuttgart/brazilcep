# -*- coding: utf-8 -*-


class CEPInvalido(Exception):
    """ Excecao disparada quando o CEP possui tamanho ioncorreto
    (diferente de 8) e/ou não existe"""
    pass
