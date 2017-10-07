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

API para consulta de CEP diretamente do *webservice* dos Correios.

> Veja também em&nbsp;
> <a href="docs/en-US/README.rst">🇺🇸</a>

Features
--------
* Consulta de dados do endereço de um CEP
* Formatacao de CEP
* Validação de estrutura do CEP

Documentação
------------

Para mais detalhes sobre a PyCEPCorreios, por gentileza, consulte a documentação oficial:

* Documentação online: https://pycep-correios.readthedocs.io.
* Documentação PDF: https://media.readthedocs.org/pdf/pycep-correios/stable/pycep-correios.pdf

Instalação
----------
O PyCEP Correios pode ser facilmente instalado com o comando a seguir:

.. code:: bash

    pip install pycep-correios

Atualmente, a PyCEPCorreios possui suporte para Python 2.7+ e 3.3+.

Como usar
---------

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios.
Veja os exemplos a seguir:

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

Aviso de *bugs*, dúvidas e sugestões
------------------------------------
Para dúvidas, sugestões e relatórios de *bugs*, por gentileza, crie uma *issue*:

- Issue Tracker: https://github.com/mstuttgart/pycep-correios/issues

Créditos
--------

Copyright (C) 2016-2017 por Michell Stuttgart Faria
