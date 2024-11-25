.. _quickstart:

Quickstart
==========

.. module:: brazilcep.client

Eager to get started? This page gives a good introduction in how to get started
with BrazilCEP.

First, make sure that:

* BrazilCEP is :ref:`installed <install>`


Let's get started with some simple examples.


Make a CEP Request
------------------

Making a request with BrazilCEP is very simple.

Begin by importing the BrazilCEP module::

    >>> import brazilcep

Now, call the `get_address_from_cep` to query any CEP::

    >>> address = brazilcep.get_address_from_cep('37503-130')

Now, we have a *dict* object called ``address``. We can
get all the address information we need from this object::

    >>> address
    {
        'district': 'rua abc',
        'cep': '37503130',
        'city': 'city ABC',
        'street': 'str',
        'uf': 'str',
        'complement': 'str',
    }

The CEP always must be a string.

Timeouts
--------

You can tell BrazilCEP to stop waiting for a response after a given number of
seconds with the ``timeout`` parameter. Nearly all production code should use
this parameter in nearly all requests. Failure to do so can cause your program
to hang indefinitely.

Proxy
-----

BrazilCEP also supports proxy setings following *requests* pattern::

    from brazilcep import get_address_from_cep

    proxies = {
        'https': "00.00.000.000",
        'http': '00.00.000.000',
    }

    # set proxies
    get_address_from_cep('37503-130', proxies=proxies)

For more details, please official `requests doc <https://requests.readthedocs.io/en/latest/user/advanced/#proxies>`_.

Unsing differents API's
-----------------------

.. note::

    BrazilCEP was developed to integrate on-demand queries into web pages.
    Querying CEP in bulk through scripts or any other means is not recommended.

.. note::

    BrazilCEP is not responsible for the functioning, availability and support of any of these query API's. All of them are provided by third parties, and
    this library just provides a handy way to centralize the CEP search on these services.

By default, BrazilCEP uses the API provided by the `OpenCEP <https://opencep.com>`_ service.

To use other services, we must indicate the desired service when calling the `get_address_from_cep`
function.

Begin by importing the BrazilCEP `Webservice` class::

    >>> from brazilcep import get_address_from_cep, WebService

Now, call the `get_address_from_cep` method with `webservice` parameter::

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

* `Webservice.APICEP`
* `Webservice.VIACEP`
* `Webservice.OPENCEP`

Errors and Exceptions
---------------------

BrazilCEP also supports a group of exceptions that can be used to
handle any errors that occur during the query process.

:exc:`~brazilcep.exceptions.InvalidCEP` exception raised by a request with invalid CEP.

:exc:`~brazilcep.exceptions.CEPNotFound` exception is raised when CEP is not find in selected API.

:exc:`~brazilcep.exceptions.BlockedByFlood`: exception raides by a large number of CEP requests in short range of time

:exc:`~brazilcep.exceptions.ConnectionError`: exception raised by a connection error.

:exc:`~brazilcep.exceptions.HTTPError`: exception raised by HTTP error.

:exc:`~brazilcep.exceptions.URLRequired`: exception raised by using a invalid URL to make a CEP request.

:exc:`~brazilcep.exceptions.TooManyRedirects`: Exception raised by too many redirects.

:exc:`~brazilcep.exceptions.Timeout`: exception raised by request timed out.

All exceptions that BrazilCEP explicitly raises inherit from :exc:`brazilcep.exceptions.BrazilCEPException`.

