Bem vindo a PyCEPCorreios!
==========================

API para consulta de CEP diretamente do *webservice* dos Correios.

A PyCEPCorreios possui as seguintes funcionalidades:

* Consulta de dados do endereço de um CEP
* Formatacao de CEP
* Validação de estrutura do CEP

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios.
Veja os exemplos a seguir:

.. code-block:: python

    import pycep_correios

    endereco = pycep_correios.consultar_cep('37503130')

    print(endereco['end'])
    print(endereco['bairro'])
    print(endereco['cidade'])
    print(endereco['complemento'])
    print(endereco['complemento2'])
    print(endereco['uf'])
    print(endereco['cep'])


.. toctree::
    :maxdepth: 2
    :hidden:
    :glob:

    installation
    usage
    contributing
    authors
    history
