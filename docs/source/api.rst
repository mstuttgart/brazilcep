.. _api:

=============
API Reference
=============

.. module:: brazilcep

This section of the documentation provides details about all the interfaces of BrazilCEP.

Client
------

The primary functionality of BrazilCEP can be accessed through the following function:

.. autofunction:: get_address_from_cep
.. autofunction:: async_get_address_from_cep

Exceptions
----------

The following exceptions are available in BrazilCEP:

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

BrazilCEP supports the following webservice integrations:

.. autofunction:: brazilcep.apicep.fetch_address
.. autofunction:: brazilcep.opencep.fetch_address
.. autofunction:: brazilcep.viacep.fetch_address

Migration from PyCEPCorreios
----------------------------

**BrazilCEP** is the new name for the former **PyCEPCorreios**. Migrating your code is simple and requires minimal changes.

1. Update the `import` statements from:

  .. code-block:: python

    import pycepcorreios

  to:

  .. code-block:: python

    import brazilcep

2. Adjust the *keys* in the query results returned by the `get_address_from_cep` function.

  The keys have been translated to English. Below is an example of the old and new formats:

  Old format:

  .. code-block:: python

    get_address_from_cep('37503-130')
    {
       'bairro': 'rua abc',
       'cep': '37503130',
       'cidade': 'city ABC',
       'logradouro': 'str',
       'uf': 'str',
       'complemento': 'str',
    }

  New format:

  .. code-block:: python

    get_address_from_cep('37503-130')
    {
       'district': 'rua abc',
       'cep': '37503130',
       'city': 'city ABC',
       'street': 'str',
       'uf': 'str',
       'complement': 'str',
    }

3. Note that the following exception has been removed:

  * `BaseException`
