"""
brazilcep.correios
~~~~~~~~~~~~~~~~

This module implements the BrazilCEP correios adapter.

:copyright: (c) 2023 by Michell Stuttgart.
:license: MIT, see LICENSE for more details.
"""

import requests
from bs4 import BeautifulSoup

from . import exceptions

URL = "https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaEndereco.cfm"

# Lista de novas chaves
address_keys = ["street", "district", "cep", "complement", "city", "uf"]


def transform_address(address: dict) -> dict:
    """Transforms an address dictionary to a new dictionary
    with standardized keys.

    Returns:
        (dict): address dict keys formated.
    """

    # Separar rua e complemento, se existir
    street, *complement = address["logradouro"].split("-", maxsplit=1)
    address["logradouro"] = street.strip()
    address["complemento"] = complement[0].strip() if complement else ""

    # Separar cidade e estado
    city, state = address.pop("localidade").split("/")
    address["municipio"] = city.strip()
    address["estado"] = state.strip()

    # Mapear valores para as novas chaves
    return {k: v.strip() for k, v in zip(address_keys, address.values())}


def extract_and_transform_cep(html: bytes) -> dict:
    """Extracts address data from HTML and transforms it into a dictionary.
    with standardized keys.

    Returns:
        (dict): respective address data.
    """

    # Analisar o HTML
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    if not table:
        return {}

    # Extrair dados da tabela
    data = {}
    for th_data, td_data in zip(table.find_all("th"), table.find_all("td")):
        # Processar chaves e valores
        key = th_data.get_text(strip=True).replace(":", "").split("/")[0].lower()
        value = td_data.get_text(strip=True)
        data[key] = value

    # Transformar e retornar o endereço
    return transform_address(data)


def fetch_address(cep, **kwargs):
    """Fetch VIACEP webservice for CEP address. VIACEP provide
    a REST API to query CEP requests.

    Args:
        cep (str):CEP to be searched.
        timeout (int): How many seconds to wait for the server to return data before giving up.
        proxies (dict):  Dictionary mapping protocol to the URL of the proxy.

    Returns:
        address (dict): respective address data from CEP.
    """
    data = {
        "CEP": cep,
    }
    response = requests.post(URL, data=data, **kwargs)  # pylint = missing-timeout

    address_data = extract_and_transform_cep(response.content)

    if address_data:
        return address_data
    raise exceptions.InvalidCEP()
