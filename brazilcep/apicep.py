"""
brazilcep.apicep
~~~~~~~~~~~~~~~~

This module implements the BrazilCEP ApiCEP adapter.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

import json

import requests

from . import exceptions

URL = "https://ws.apicep.com/cep/{}.json"


def fetch_address(cep):
    """Fetch VIACEP webservice for CEP address. VIACEP provide
    a REST API to query CEO requests.

    Args:
        cep (str):CEP to be searched.

    Returns:
        address (dict): respective address data from CEP.
    """

    response = requests.get(URL.format(cep), timeout=5)

    if response.status_code == 200:
        # Transforma o objeto requests em um dict
        address = json.loads(response.text)

        if (
            address["status"] == 400
            and address["message"] == "CEP informado é inválido"
        ):
            raise exceptions.InvalidCEP()

        if address["status"] == 400 and address["message"] == "Blocked by flood":
            raise exceptions.BlockedByFlood()

        if address["status"] == 404:
            raise exceptions.CEPNotFound()

        return {
            "district": address.get("district") or "",
            "cep": address.get("code") or "",
            "city": address.get("city") or "",
            "street": (address.get("address") or "").split(" - até")[0],
            "uf": address.get("state") or "",
            "complement": "",
        }

    raise exceptions.BrazilCEPException(
        f"Other error. Status code: {response.status_code}"
    )
