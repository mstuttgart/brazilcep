PyCEPCorreios
=============


[![Build Status](https://img.shields.io/travis/mstuttgart/pycep-correios/develop.svg?style=flat-square)](https://travis-ci.org/mstuttgart/pycep-correios)

[![Coverage Status](https://img.shields.io/coveralls/mstuttgart/pycep-correios/develop.svg?style=flat-square)](https://coveralls.io/github/mstuttgart/pycep-correios?branch=develop)

[![Health Status](https://landscape.io/github/mstuttgart/pycep-correios/develop/landscape.svg?style=flat-square)](https://landscape.io/github/mstuttgart/pycep-correios/develop)

[![pypi](https://img.shields.io/pypi/v/pycep-correios.svg?style=flat-square)](https://pypi.python.org/pypi/pycep-correios)

[![python versions](https://img.shields.io/pypi/pyversions/pycep-correios.svg?style=flat-square)](https://pypi.python.org/pypi/pycep-correios)

[![licences](https://img.shields.io/pypi/l/pycep-correios.svg?style=flat-square)](https://github.com/mstuttgart/pycep-correios/blob/develop/LICENSE)


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

    $pip install pycep-correios


Currently, the PyCEPCorreios supports Python 2.7+ and 3.3+.

Usage
-----

To find the address from CEP is a very simple job with PyCEPCorreios.

Check this example:

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