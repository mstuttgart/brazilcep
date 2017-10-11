==========
Usage
==========

Searching an address using CEP code is very simple with PyCEPCorreios. It was made to make the usage as simpler as possible.

Consulting CEP
---------------

Search by CEP code is done by the `consultar_cep` function.

.. code:: python

    import pycep_correios

    address = pycep_correios.consultar_cep('37503130')

    print(address['end'])
    print(address['bairro'])
    print(address['cidade'])
    print(address['complemento'])
    print(address['complemento2'])
    print(address['uf'])
    print(address['cep'])

This function returns a `dict` with the data of the address and has the following values:

* **end**: street name
* **bairro**: neighborhood
* **cidade**: city name
* **complemento**: address complement
* **complemento2**: similar to `complemento`, can show the range of house numbers within the CEP.
* **uf**: state (`SP` for São Paulo, `MG` for Minas Gerais, etc.)
* **cep**: the CEP code

Check the example, searching cep code `37503130` gives us the following:

.. code:: python

    >>> print(address)
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

The command also accepts CEP codes with dots and/or hiphen. As example:

.. code:: python

    import pycep_correios

    address = pycep_correios.consultar_cep('37.503-130')

This is useful for external applications using PyCEPCorreios. They can send requests to PyCEPCorreios.
The CEP code will always be formatted to the ECT *webservice*.

When consulting a CEP with wrong format (number of digits different of 8) or a code that
doesn't exist, the exception `CEPInvalido` is raised. 

From version 2.2.0, PyCEPCorreios implements new types of exceptions. They are: *Timout*, *FalhaNaConexao*, *MultiploRedirecionamento*
All of those exceptions extends from the new base exception *ExcecaoPyCEPCorreios*:

.. code:: python

    from pycep_correios import consultar_cep
    from pycep_correios.excecoes import (CEPInvalido,
                                         ExcecaoPyCEPCorreios,
                                         Timeout,
                                         MultiploRedirecionamento,
                                         FalhaNaConexao)

    try:        
        address = pycep_correios.consultar_cep('00000000')
        
    except Timeout as exc:
        print(exec)
        
    except FalhaNaConexao as exc:
        print(exc)
        
    except MultiploRedirecionamento as exc:
        print(exc)
        
    except CEPInvalido as exc:
        print(exc)
        
    except ExcecaoPyCEPCorreios as exc:
        print(exc)

You can also choose in which *webservice* you want the query to be run. Homologation or production *webservice* of Correios.
This feature can be useful when you are using PyCEPCorreios in development environment.

To run the search in development environment you just need to set the `ambiente` parameter in the function.
For development, set the parameter to `HOMOLOGACAO`:

.. code:: python

    from pycep_correios import consultar_cep
    from pycep_correios import HOMOLOGACAO, PRODUCAO

    # Run the search in homologation environment
    address = consultar_cep(cep='37503130', ambiente=HOMOLOGACAO)

    # Run the search in production environment
    address = consultar_cep(cep='37503130', ambiente=PRODUCAO)

`PRODUCAO` is the *default* value of `ambiente`. If you are running in production, don't need to set the `ambiente=PRODUCAO`.

**NOTE**: If you set some value different from `HOMOLOGACAO` or `PRODUCAO`, a `KeyError` exception will be thrown.

Validating CEP
--------------

CEP code validation can be done with `validar_cep` command. That function returns
`True` if the code is correct and `False` otherwise.

.. code:: python

    import pycep_correios

    cep_code = '37.503-003'

    if pycep_correios.validar_cep(cep_code):
        print('The CEP code %s is valid!!' % cep_code)
    else:
        print('Ops!! The CEP code %s is not valid!!' % cep_code)

That function also accepts CEP codes with punctuation: `37.503-003`.

CEP code Formatting
-------------------

The function `formatar_cep` gets a string with CEP code and removes dots and hiphens.
That function is used internally by `consultar_cep`.

.. code:: python

    from pycep_correios import formatar_cep

    cep_code = '37.503-003'

    try:
        formatted_cep = formatar_cep(cep_code)
        print('The CEP code %s formatted: %s' % (cep_code, formatted_cep))
    except ValueError as exc:
        print('Error formatting CEP code: %s' % exc)
