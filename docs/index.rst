Bem vindo PyCEPCorreios!
========================

API para consulta de CEP diretamente do *webservice* dos Correios.

A PyCEPCorreios possui as seguintes funcionalidades para ajudar o desenvolvedor
a trabalhar com consultas de CEPs.

* Consulta de dados do endereço de um CEP
* Formatacao de CEP
* Validação de estrutura do CEP

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios.
Veja os exemplos a seguir:

.. code-block:: python

    >>> import pycep_correios

    >>> pycep_correios.validar_cep('37503130')
    True

    >>> endereco = pycep_correios.consultar_cep('37503130')
    >>> print(endereco['end'])
    >>> print(endereco['bairro'])
    >>> print(endereco['cidade'])
    >>> print(endereco['complemento'])
    >>> print(endereco['complemento2'])
    >>> print(endereco['uf'])
    >>> print(endereco['cep'])


.. toctree::
    :maxdepth: 2
    :hidden:
    :glob:

    installation
    usage
    contributing
    authors
    history
