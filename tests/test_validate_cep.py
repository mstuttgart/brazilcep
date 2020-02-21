import pytest

from pycep_correios import validar_cep


def test_success():

    assert validar_cep('37.503-003')
    assert validar_cep('   37.503-003')
    assert validar_cep('37.503&003saasd')

    assert not validar_cep('37.503-00')


def test_fail():

    with pytest.raises(ValueError):
        validar_cep(37503003)

    with pytest.raises(ValueError):
        validar_cep('')
