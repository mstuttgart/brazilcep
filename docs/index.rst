Bem vindo a PyCEPCorreios!
==========================

.. image:: https://img.shields.io/pypi/v/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/pyversions/pycep-correios.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pycep-correios

.. image:: https://img.shields.io/pypi/l/pycep-correios.svg?style=flat-square
    :target: https://github.com/mstuttgart/pycep-correios/blob/develop/LICENSE

A PyCEPCorreios é uma API para consulta de CEP no *webservice* ViaCep.

A PyCEPCorreios possui as seguintes funcionalidades:

* Consulta de dados do endereço de um CEP
* Formatação de CEP
* Validação de estrutura do CEP

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios.
Veja o exemplo a seguir:

.. code-block:: python

    >>> import pycep_correios

    >>> endereco = pycep_correios.get_address_from_cep('37503130')
    >>> print(endereco)
    {
        'bairro': 'Santo Antônio',
        'cep': '37503130',
        'cidade': 'Itajubá',
        'logradouro': 'Rua Geraldino Campista',
        'uf': 'MG',
        'complemento': '- até 214/215',
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

Encontrou algum erro? Tem alguma sugestão para melhorar a PyCEPCorreios? Deixe-me saber.
Contribuições são muito bem vindas!