import pytest

from pycep_correios import format_cep


def test_success():

    assert format_cep('37.503-003') == '37503003'
    assert format_cep('   37.503-003') == '37503003'
    assert format_cep('37 503-003') == '37503003'
    assert format_cep('37.503&003saasd') == '37503003'
    assert format_cep('\n \r 37.503-003') == '37503003'
    assert format_cep('\n \r 37.503-003') == '37503003'

    # ponto e virgula
    assert format_cep('37.503-003;') == '37503003'

    # Unicode Greek Question Mark
    assert format_cep(u'37.503-003;') == '37503003'


def test_fail():

    with pytest.raises(ValueError):
        format_cep(37503003)

    with pytest.raises(ValueError):
        format_cep('')

    with pytest.raises(ValueError):
        format_cep(None)

    with pytest.raises(ValueError):
        format_cep(False)

    with pytest.raises(ValueError):
        format_cep(True)
