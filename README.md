<h2 align="center">
  <a href="https://pypi.org/project/brazilcep/">
    <img src="https://github.com/mstuttgart/brazilcep/assets/8174740/fb7c86c8-6261-4300-b2e0-65877084d865" width="15%">
  </a>
  <br>
      BrazilCEP
</h2>

<p align="center">

  <a href="https://github.com/mstuttgart/brazilcep/actions?query=workflow%3A%22Github+CI%22">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/mstuttgart/brazilcep/test.yml?color=fcd800&branch=main">
  </a>

 <a href="https://codecov.io/gh/mstuttgart/brazilcep" >
  <img alt="Codecov" src="https://img.shields.io/codecov/c/github/mstuttgart/brazilcep?color=fcd800">
 </a>

<a href="https://brazilcep.readthedocs.io/" >
  <img alt="readthedocs" src="https://img.shields.io/readthedocs/brazilcep?color=fcd800">
 </a>

  <a href="https://pypi.org/project/brazilcep">
    <img src="https://img.shields.io/pypi/dm/brazilcep?color=fcd800" alt="Downloads">
  </a>

  <a href="https://pypi.org/project/brazilcep">
    <img src="https://img.shields.io/pypi/v/brazilcep.svg?" alt="Ratings">
  </a>

  <a href="https://pypi.org/project/brazilcep/">
    <img src="https://img.shields.io/pypi/pyversions/brazilcep.svg" alt="Version">
  </a>

</p>

<p align="center">
  <a href="#about">About</a> |
  <a href="#install">Install</a> |
  <a href="#quick-start">How to Use</a> |
  <a href="#documentation">Documentation</a> |
  <a href="#contribute">Contribute</a> |
  <a href="#credits">Credits</a>
</p>

## About

**BrazilCEP** is a minimalist and easy-to-use Python library designed to query CEP (Postal Address Code) data.

Its objective is to provide a common query interface to all these search services, facilitating the integration of Python applications with these services.

Currently supports several CEP API's:

- [ViaCEP](https://viacep.com.br)
- [ApiCEP (WideNet)](https://apicep.com)
- [OpenCEP](https://opencep.com/)

> [!NOTE]
> **BrazilCEP** is the new name of former **PyCEPCorreio** Python library.
> If you want to migrate the old code to the new version, please see the [migrate](https://brazilcep.readthedocs.io/api.html#migrate-from-pycepcorreios) section in docs.

> [!TIP]
> **CEP** or **Código de Endereçamento Postal** (_Postal Address Code_), as it is also known, is a system of numeric codes, created, maintained and organized by _Correios do Brazil_ for
> organizing addresses and deliveries of letters and parcels.

## Install

The recommended way to get BrazilCEP is to **install the latest stable release**
via [pip](http://pip-installer.org>):

```sh
pip install brazilcep
```

## Quick Start

Making a request is very simple. Begin by importing the BrazilCEP module:

```python
>>> import brazilcep
```

Now, call the `get_address_from_cep` to query any CEP:

```python
>>> address = brazilcep.get_address_from_cep('37503-130')
```

Now, we have a _dict_ object called `address`. We can
get all the address information we need from this object:

```python
 >>> address
{
    'district': 'rua abc',
    'cep': '37503130',
    'city': 'city ABC',
    'street': 'str',
    'uf': 'str',
    'complement': 'str',
}
```

The CEP always must be a string.

> [!TIP]
> BrazilCEP was developed to integrate on-demand queries into web pages.
> Querying CEP in bulk through scripts or any other means is not recommended.

> [!IMPORTANT]
> BrazilCEP is not responsible for the functioning, availability and support of any of these query API's.
> All of them are provided by third parties, and this library just provides a handy way to centralize the CEP search on these services.

## Documentation

Documentation for the current version of BrazilCEP is available [here](https://brazilcep.readthedocs.io/).

## Contribute

See this _guideline_ [here](https://brazilcep.readthedocs.io/contributing.html).

## Credits

Copyright (C) 2016-2024 by Michell Stuttgart
