"""
brazilcep.viacep
~~~~~~~~~~~~~~~~

This module implements the BrazilCEP ViaCEP adapter.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

import json

import requests

from . import exceptions

URL = "http://www.viacep.com.br/ws/{}/json"


def fetch_address(cep, **kwargs):
    """Fetch APICEP webservice for CEP address. APICEP provide
    a REST API to query CEP requests.

    Args:
        cep (str):CEP to be searched.
        timeout (int): How many seconds to wait for the server to return data before giving up.
        proxies (dict):  Dictionary mapping protocol to the URL of the proxy.


    Returns:
        address (dict): respective address data from CEP.
    """

    response = requests.get(URL.format(cep), **kwargs)  # pylint = missing-timeout

    if response.status_code == 200:
        # Transforma o objeto requests em um dict
        address = json.loads(response.text)

        if address.get("erro"):
            raise exceptions.CEPNotFound()

        return {
            "district": address.get("bairro") or "",
            "cep": address.get("cep") or "",
            "city": address.get("localidade") or "",
            "street": address.get("logradouro") or "",
            "uf": address.get("uf") or "",
            "complement": address.get("complemento") or "",
        }

    if response.status_code == 400:
        raise exceptions.InvalidCEP()

    raise exceptions.BrazilCEPException(
        f"Other error. Status code: {response.status_code}"
    )
