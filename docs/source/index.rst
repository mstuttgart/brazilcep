
BrazilCEP: Query CEP Easily™
============================

.. image:: https://static.pepy.tech/badge/brazilcep/month
    :target: https://pepy.tech/project/brazilcep/
    :alt: BrazilCEP Downloads Per Month Badge

.. image:: https://img.shields.io/pypi/l/brazilcep.svg
    :target: https://pypi.org/project/brazilcep/
    :alt: License Badge

.. image:: https://img.shields.io/pypi/v/brazilcep.svg
    :target: https://pypi.org/project/brazilcep/
    :alt: BrazilCEP Version Badge

.. image:: https://img.shields.io/pypi/pyversions/brazilcep.svg
    :target: https://pypi.org/project/brazilcep/
    :alt: Python Version Support Badge

**BrazilCEP** is a minimalist and easy-to-use Python library designed to query CEP (Postal Address Code) data.

-------------------

A simple use example::

    >>> brazilcep.get_address_from_cep('37503-130')
    {
        'district': 'rua abc',
        'cep': '37503130',
        'city': 'city ABC',
        'street': 'str',
        'uf': 'str',
        'complement': 'str',
    }


**BrazilCEP** objective is to provide a common query interface to all these search services, facilitating the integration of Python applications with these services.

Currently supports several CEP API's:

- `ViaCEP <https://viacep.com.br>`_.
- `ApiCEP (WideNet) <https://apicep.com>`_.
- `OpenCEP <https://opencep.com/>`_.

**CEP** or **Código de Endereçamento Postal** (*Postal Address Code*), as it is also known, is a system of numeric codes, 
created, maintained and organized by *Correios do Brazil* for organizing addresses and deliveries of letters and parcels.

The User Guide
--------------

This part of the documentation, which is mostly prose, begins with some
background information about BRazilCEP.

.. toctree::
   :maxdepth: 2

   user/install
   user/quickstart

The API Documentation / Guide
-----------------------------

If you are looking for information on a specific function, class, or method,
this part of the documentation is for you.

.. toctree::
   :maxdepth: 2

   api


The Contributor Guide
---------------------

If you want to contribute to the project, this part of the documentation is for
you.

.. toctree::
   :maxdepth: 3

   dev/contributing

Release History
---------------

.. toctree::
   :maxdepth: 1

   changes
