
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

---

Quick Example
-------------

A simple usage example::

    >>> import brazilcep
    >>> brazilcep.get_address_from_cep('37503-130')
    {
        'district': 'rua abc',
        'cep': '37503130',
        'city': 'city ABC',
        'street': 'str',
        'uf': 'str',
        'complement': 'str',
    }

**BrazilCEP** aims to provide a unified query interface for various CEP search services, simplifying the integration of Python applications with these services.

Supported CEP APIs
------------------

Currently, BrazilCEP supports the following CEP APIs:

- `ViaCEP <https://viacep.com.br>`_
- `ApiCEP (WideNet) <https://apicep.com>`_
- `OpenCEP <https://opencep.com/>`_

What is CEP?
------------

**CEP** or **Código de Endereçamento Postal** (*Postal Address Code*) is a system of numeric codes created, maintained, and organized by *Correios do Brazil* to streamline the organization of addresses and the delivery of letters and parcels.

Documentation Overview
----------------------

The User Guide
~~~~~~~~~~~~~~

This section provides background information and step-by-step instructions for using BrazilCEP.

.. toctree::
   :maxdepth: 2

   user/install
   user/quickstart

The API Documentation
~~~~~~~~~~~~~~~~~~~~~

For details on specific functions, classes, or methods, refer to this section.

.. toctree::
   :maxdepth: 2

   api

The Contributor Guide
~~~~~~~~~~~~~~~~~~~~~

If you want to contribute to the project, this section provides all the necessary guidelines.

.. toctree::
   :maxdepth: 3

   contributing

Release History
~~~~~~~~~~~~~~~

For a detailed changelog of the project, see this section.

.. toctree::
   :maxdepth: 1

   changes

