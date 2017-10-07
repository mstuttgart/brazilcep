=============
PyCEPCorreios
=============

.. image:: https://img.shields.io/travis/mstuttgart/pycep-correios/develop.svg?style=flat-square
    :target: https://travis-ci.org/mstuttgart/pycep-correios

.. image:: https://img.shields.io/coveralls/mstuttgart/pycep-correios/develop.svg?style=flat-square
    :target: https://coveralls.io/github/mstuttgart/pycep-correios?branch=develop

.. image:: https://landscape.io/github/mstuttgart/pycep-correios/develop/landscape.svg?style=flat-square
    :target: https://landscape.io/github/mstuttgart/pycep-correios/develop

.. image:: https://img.shields.io/pypi/v/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/pyversions/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/l/pycep-correios.svg?style=flat-square
    :target: https://github.com/mstuttgart/pycep-correios/blob/develop/LICENSE


API for querying CEP (zip code) from Correios (Brazilian Mail Service) webservices

Features
--------
* Find address data from CEP
* CEP formatting
* CEP validation

Documentation
-------------

For further information, please, fell free to reach the official documentation:

* On-line: https://pycep-correios.readthedocs.io.
* PDF file: https://media.readthedocs.org/pdf/pycep-correios/stable/pycep-correios.pdf


Installing
----------
One can easily install the PyCEP running the following command:

.. code:: bash

    pip install pycep-correios


Currently, the PyCEPCorreios supports Python 2.7+ and 3.3+.

Usage
-----

To find the address from CEP is a very simple job with PyCEPCorreios.

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

How to Contribute
-----------------
To send questions, suggestions and *bug* reports, please, create an *issue*:

- Issue Tracker: https://github.com/mstuttgart/pycep-correios/issues

Credits
-------

Copyright (C) 2016-2017 por Michell Stuttgart Faria
