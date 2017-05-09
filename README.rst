PyCEP Correios
==============

.. image:: https://img.shields.io/travis/mstuttgart/pycep-correios/master.svg?style=flat-square
    :target: https://travis-ci.org/mstuttgart/pycep-correios

.. image:: https://img.shields.io/coveralls/mstuttgart/pycep-correios/master.svg?style=flat-square
    :target: https://coveralls.io/github/mstuttgart/pycep-correios?branch=master

.. image:: https://landscape.io/github/mstuttgart/pycep-correios/master/landscape.svg?style=flat-square
    :target: https://landscape.io/github/mstuttgart/pycep-correios/master

.. image:: https://img.shields.io/pypi/v/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/pyversions/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/l/pycep-correios.svg?style=flat-square
    :target: https://github.com/mstuttgart/pycep-correios/blob/develop/LICENSE

.. image:: https://readthedocs.org/projects/pycep-correios/badge/?style=flat-square
    :target: http://pycep-correios.readthedocs.io/pt/latest/?badge=latest

O PyCEP Correios faz uso do webservice dos correios para efetuar a busca de um dado CEP fornecido pelo usuário. O retorno dessa consulta é o endereço pertencente ao CEP.

Instalação
==========
O PyCEP Correios pode ser facilmente instalado com o comando a seguir:

.. code:: bash
    pip3 install pycep-correios


Como usar
---------

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios. Não importa se o CEP fornecido possui hífen ou ponto. O PyCEPCorreios trata a entrada garantindo uma entrada válida para o *webservice* dos Correios.
Veja os exemplos a seguir:

.. code:: python

    from pycep_correios.correios import Correios
    from pycep_correios.correios_exceptions import CorreiosCEPInvalidCEPException

    # Tambem pode ser usado .get_cep('37503130')
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

Aviso de *bugs*, dúvidas e sugestões
====================================
Para dúvidas, sugestões e relatórios de *bugs*, por gentileza, crie uma *issue*:

- Issue Tracker: https://github.com/mstuttgart/pycep-correios/issues

Contribuidores
==============
Meus agradecimentos aos seguintes contribuidores:

* `Aldo Soares <https://github.com/aldo774>`_
* `Felipe Morato <https://github.com/fmorato>`_

Créditos
========

Copyright (C) 2015-2017 por Michell Stuttgart Faria
