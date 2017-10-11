Welcome to PyCEPCorreios!
==========================
.. image:: https://img.shields.io/pypi/v/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/pyversions/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/l/pycep-correios.svg?style=flat-square
    :target: https://github.com/mstuttgart/pycep-correios/blob/develop/LICENSE

PyCEPCorreios is an API for querying CEP (zip code) from Correios (Brazilian Mail Service) webservices.
The *webservice* used to search CEP code is the SIGEPWeb, provided by ECT (Empresa de Correios e Telégrafos - Brazilian Mail Service).

The PyCEPCorreios has as main features:
---------------------------------------
* Find address data from CEP
* CEP formatting
* CEP validation

To find an address from a CEP code is a very simple job with PyCEPCorreios.
Check this example:

.. code-block:: python

    >>> import pycep_correios

    >>> endereco = pycep_correios.consultar_cep('37503130')
    >>> print(endereco)
    {
        'bairro': 'Santo Antônio',
        'cep': '37503130',
        'cidade': 'Itajubá',
        'end': 'Rua Geraldino Campista',
        'id': '0',
        'uf': 'MG',
        'complemento': '',
        'complemento2': '- até 214/215',
    }


.. toctree::
    :maxdepth: 2
    :hidden:
    :glob:

    installation
    usage
    contributing
    authors
    history

Found any bugs? Want to contribute with suggestions to PyCEPCorreios? Keep in touch.
Contributions are very welcome!