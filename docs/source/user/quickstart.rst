.. _quickstart:

Quickstart
==========

.. module:: brazilcep.client

Eager to get started? This page provides a quick introduction to using BrazilCEP.

First, ensure that:

* BrazilCEP is :ref:`installed <install>`

Let's dive into some simple examples.

Make a CEP Request
------------------

Making a request with BrazilCEP is straightforward.

Start by importing the BrazilCEP module::

    >>> import brazilcep

Next, use the `get_address_from_cep` function to query any CEP::

    >>> address = brazilcep.get_address_from_cep('37503-130')

The result is a *dict* object called ``address``. You can retrieve all the address information you need from this object::

    >>> address
    {
        'district': 'rua abc',
        'cep': '37503130',
        'city': 'city ABC',
        'street': 'str',
        'uf': 'str',
        'complement': 'str',
    }

**Note:** The CEP must always be a string.

Timeouts
--------

You can specify a timeout for BrazilCEP requests using the ``timeout`` parameter. This is highly recommended for production code to prevent your program from hanging indefinitely.

Proxy
-----

BrazilCEP supports proxy settings following the *requests* library pattern::

    from brazilcep import get_address_from_cep

    proxies = {
        'https': "00.00.000.000",
        'http': '00.00.000.000',
    }

    # Set proxies
    get_address_from_cep('37503-130', proxies=proxies)

For more details, refer to the official `requests documentation <https://requests.readthedocs.io/en/latest/user/advanced/#proxies>`_.

Using Different APIs
---------------------

.. note::

    BrazilCEP is designed for on-demand queries, such as integration into web pages. Bulk querying of CEPs through scripts or other means is not recommended.

.. note::

    BrazilCEP is not responsible for the functionality, availability, or support of any third-party query APIs. This library simply provides a centralized way to search for CEPs using these services.

By default, BrazilCEP uses the API provided by the `OpenCEP <https://opencep.com>`_ service.

To use other services, specify the desired service when calling the `get_address_from_cep` function.

Start by importing the BrazilCEP `WebService` class::

    >>> from brazilcep import get_address_from_cep, WebService

Then, call the `get_address_from_cep` method with the `webservice` parameter::

    >>> get_address_from_cep('37503-130', webservice=WebService.APICEP)
    {
      'district': 'rua abc',
      'cep': '37503130',
      'city': 'city ABC',
      'street': 'str',
      'uf': 'str',
      'complement': 'str',
    }

The possible values for the `webservice` parameter are:

* `WebService.APICEP`
* `WebService.VIACEP`
* `WebService.OPENCEP`

Errors and Exceptions
---------------------

BrazilCEP provides a set of exceptions to handle errors during the query process:

- :exc:`~brazilcep.exceptions.InvalidCEP`: Raised when an invalid CEP is provided.
- :exc:`~brazilcep.exceptions.CEPNotFound`: Raised when the CEP is not found in the selected API.
- :exc:`~brazilcep.exceptions.BlockedByFlood`: Raised when too many CEP requests are made in a short period.
- :exc:`~brazilcep.exceptions.ConnectionError`: Raised when a connection error occurs.
- :exc:`~brazilcep.exceptions.HTTPError`: Raised when an HTTP error occurs.
- :exc:`~brazilcep.exceptions.URLRequired`: Raised when an invalid URL is used for a CEP request.
- :exc:`~brazilcep.exceptions.TooManyRedirects`: Raised when too many redirects occur.
- :exc:`~brazilcep.exceptions.Timeout`: Raised when a request times out.

All exceptions explicitly raised by BrazilCEP inherit from :exc:`brazilcep.exceptions.BrazilCEPException`.
