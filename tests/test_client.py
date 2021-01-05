
import pytest

from pycep_correios import get_address_from_cep
from pycep_correios.client import _format_cep


def test_search_error():

    with pytest.raises(KeyError):
        get_address_from_cep('37.503-130', webservice=5)

    with pytest.raises(KeyError):
        get_address_from_cep('37.503-130', webservice='VIACEP')


def test_format_cep_success():

    assert _format_cep('37.503-003') == '37503003'
    assert _format_cep('   37.503-003') == '37503003'
    assert _format_cep('37 503-003') == '37503003'
    assert _format_cep('37.503&003saasd') == '37503003'
    assert _format_cep('\n \r 37.503-003') == '37503003'
    assert _format_cep('\n \r 37.503-003') == '37503003'

    # ponto e virgula
    assert _format_cep('37.503-003;') == '37503003'

    # Unicode Greek Question Mark
    assert _format_cep(u'37.503-003;') == '37503003'


def test_format_cep_fail():

    with pytest.raises(ValueError):
        _format_cep(37503003)

    with pytest.raises(ValueError):
        _format_cep('')

    with pytest.raises(ValueError):
        _format_cep(None)

    with pytest.raises(ValueError):
        _format_cep(False)

    with pytest.raises(ValueError):
        _format_cep(True)
