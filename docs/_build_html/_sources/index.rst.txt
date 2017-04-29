.. PyCEP Correios documentation master file, created by
   sphinx-quickstart on Fri Apr 21 16:28:07 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

PyCEP Correios
==============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. image:: https://img.shields.io/travis/mstuttgart/pycep-correios/master.svg?style=flat-square
    :target: https://travis-ci.org/mstuttgart/pycep-correios

.. image:: https://img.shields.io/coveralls/mstuttgart/pycep-correios/master.svg?style=flat-square
    :target: https://coveralls.io/github/mstuttgart/pycep-correios?branch=master
    :alt: coveralls.io

.. image:: https://landscape.io/github/mstuttgart/pycep-correios/master/landscape.svg?style=flat-square
    :target: https://landscape.io/github/mstuttgart/pycep-correios/master

.. image:: https://img.shields.io/pypi/v/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/pyversions/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/wheel/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/l/pycep-correios.svg?style=flat-square
    :target: https://github.com/mstuttgart/pycep-correios/blob/master/LICENSE

O PyCEP Correios faz uso do webservice dos correios para efetuar a busca de um dado CEP fornecido pelo usuário. O retorno dessa consulta é o endereço pertencente ao CEP.

Instalação
----------
O PyCEP Correios atualmente está disponível apenas para Python 3. Ele pode ser facilmente instalado com o comando a seguir::

    pip3 install pycep-correios

Como usar
---------

Consultar o endereço de um CEP é muito simples com o *PyCEPCorreios*.

Não importa se o CEP fornecido possui hífen ou ponto. O PyCEPCorreios trata a entrada garantindo uma entrada válida para o *webservice* dos Correios.

Veja os exemplos a seguir::

    from pycep_correios.correios import Correios
    from pycep_correios.correios_exceptions import CorreiosCEPInvalidCEPException

    # Consultando CEP 37503130
    endereco = Correios.get_cep('37503130')

    print(endereco['rua'])
    print(endereco['bairro'])
    print(endereco['cidade'])
    print(endereco['complemento'])
    print(endereco['uf'])
    print(endereco['outro'])

    # Terceiro exemplo, usando o mesmo cep usado anteriormente, porém com hífen e ponto.
    endereco = Correios.get_cep('37.503-130')

    print(endereco['rua'])
    print(endereco['bairro'])
    print(endereco['cidade'])
    print(endereco['complemento'])
    print(endereco['uf'])
    print(endereco['outro'])

    # Quarto exemplo, enviamos um cep incorreto, com o numero de digitos inferior a 8.

    try:
        endereco = Correios.get_cep('37.50-130')
    except CorreiosCEPInvalidCEPException as exc:
        print(exc.message)

Contribuições
-------------

Aviso de erros e sugestões: `github.com/mstuttgart/pycep-correios/issues <github.com/mstuttgart/pycep-correios/issues>`_

Contribuidores
--------------
Meus agradecimentos aos seguintes contribuidores, por tornar o PyCEP Correios melhor:

* `Aldo Soares <https://github.com/Aldo774>`_

Créditos
--------

Copyright (C) 2015-2017 por Michell Stuttgart Faria
