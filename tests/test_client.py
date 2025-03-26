import pytest

from brazilcep import get_address_from_cep
from brazilcep.client import _format_cep


def test_search_error():
    """
    Test that invalid webservice values raise a KeyError.
    """
    invalid_webservices = [5, "VIACEP"]

    for webservice in invalid_webservices:
        with pytest.raises(KeyError):
            get_address_from_cep("37.503-130", webservice=webservice)


def test_format_cep_success():
    """
    Test that _format_cep correctly formats valid CEP inputs.
    """
    test_cases = [
        ("37.503-003", "37503003"),
        ("   37.503-003", "37503003"),
        ("37 503-003", "37503003"),
        ("37.503&003saasd", "37503003"),
        ("\n \r 37.503-003", "37503003"),
        ("37.503-003;", "37503003"),  # Semicolon
        ("37.503-003;", "37503003"),  # Unicode Greek Question Mark
    ]

    for input_cep, expected_output in test_cases:
        assert _format_cep(input_cep) == expected_output


def test_format_cep_fail():
    """
    Test that _format_cep raises a ValueError for invalid inputs.
    """
    invalid_inputs = [37503003, "", None, False, True]
    for invalid_input in invalid_inputs:
        with pytest.raises(ValueError):
            _format_cep(invalid_input)
