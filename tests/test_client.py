from warnings import catch_warnings

import pytest

from brazilcep import WebService, get_address_from_cep
from brazilcep.client import _format_cep


def test_search_error():
    with pytest.raises(KeyError):
        get_address_from_cep("37.503-130", webservice=5)

    with pytest.raises(KeyError):
        get_address_from_cep("37.503-130", webservice="VIACEP")


def test_format_cep_success():
    assert _format_cep("37.503-003") == "37503003"
    assert _format_cep("   37.503-003") == "37503003"
    assert _format_cep("37 503-003") == "37503003"
    assert _format_cep("37.503&003saasd") == "37503003"
    assert _format_cep("\n \r 37.503-003") == "37503003"
    assert _format_cep("\n \r 37.503-003") == "37503003"

    # ponto e virgula
    assert _format_cep("37.503-003;") == "37503003"

    # Unicode Greek Question Mark
    assert _format_cep("37.503-003;") == "37503003"


def test_format_cep_fail():
    with pytest.raises(ValueError):
        _format_cep(37503003)

    with pytest.raises(ValueError):
        _format_cep("")

    with pytest.raises(ValueError):
        _format_cep(None)

    with pytest.raises(ValueError):
        _format_cep(False)

    with pytest.raises(ValueError):
        _format_cep(True)


def test_a_deprecated_enum_value():
    with catch_warnings(record=True) as w:
        # ADeprecatedEnum.FOO is not deprecated and should not throw any warning
        get_address_from_cep("37.503-130", webservice=WebService.OPENCEP)
        assert len(w) == 0

        # ADeprecatedEnum.BAR is deprecated and we expect to have a warning raised.
        get_address_from_cep("37.503-130", webservice=WebService.CORREIOS)
        assert len(w) == 1
        assert issubclass(w[0].category, DeprecationWarning)
        assert (
            str(w[0].message) == "CORREIOS is going to be deprecated. Please, use other webservice."
        )
