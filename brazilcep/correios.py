"""
brazilcep.correios
~~~~~~~~~~~~~~~~

This module implements the BrazilCEP Correios adapter.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

import zeep

from . import exceptions

URL = "https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl"  # noqa


def fetch_address(cep):
    """Fetch CORREIOS webservice for CEP address. CORREIOS provide
    a SOAP to query CEO requests.

    Args:
        cep (str):CEP to be searched.

    Returns:
        address (dict): respective address data from CEP.
    """

    try:

        client = zeep.Client(URL)

        address = client.service.consultaCEP(cep)

        return {
            "district": getattr(address, "bairro") or "",
            "cep": getattr(address, "cep") or "",
            "city": getattr(address, "cidade") or "",
            "street": getattr(address, "end") or "",
            "uf": getattr(address, "uf") or "",
            "complement": getattr(address, "complemento2") or "",
        }

    except zeep.exceptions.Fault as err:
        raise exceptions.BrazilCEPException(err)
