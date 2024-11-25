.. _api:

=============
API Reference
=============

.. module:: brazilcep

This part of the documentation covers all the interfaces of BrazilCEP. 

Client
------

The main BrazilCEP' functionality can be accessed by this function.

.. autofunction:: get_address_from_cep

Exceptions
----------

.. autoexception:: brazilcep.exceptions.BrazilCEPException
.. autoexception:: brazilcep.exceptions.ConnectionError
.. autoexception:: brazilcep.exceptions.HTTPError
.. autoexception:: brazilcep.exceptions.URLRequired
.. autoexception:: brazilcep.exceptions.TooManyRedirects
.. autoexception:: brazilcep.exceptions.Timeout
.. autoexception:: brazilcep.exceptions.InvalidCEP
.. autoexception:: brazilcep.exceptions.CEPNotFound
.. autoexception:: brazilcep.exceptions.BlockedByFlood

Webservices
-----------

.. autofunction:: brazilcep.apicep.fetch_address
.. autofunction:: brazilcep.opencep.fetch_address
.. autofunction:: brazilcep.viacep.fetch_address


Migrate from PyCEPCorreios
--------------------------

**BrazilCEP** is the new name of former **PyCEPCorreios**. It's simples migrate te code and require minimal steps.

First, rename the `import` statements from::

  >>> import pycepcorreios

to::

  >>> import brazilcep

The next step, is adjust the *keys* of query returned by `get_address_from_cep` function.

The keys have simply been translated to english. Take a look on this old code::

    >>> get_address_from_cep('37503-130')
    {
      'bairro': 'rua abc',
      'cep': '37503130',
      'cidade': 'city ABC',
      'logradouro': 'str',
      'uf': 'str',
      'complemento': 'str',
    }

This is the new code::

    >>> get_address_from_cep('37503-130')
    {
      'district': 'rua abc',
      'cep': '37503130',
      'city': 'city ABC',
      'street': 'str',
      'uf': 'str',
      'complement': 'str',
    }

The follow `Exceptions` have been removed:

* `BaseException`

