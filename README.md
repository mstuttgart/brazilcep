
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

  <a href="https://www.codefactor.io/repository/github/mstuttgart/brazilcep">
    <img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/mstuttgart/brazilcep/main?color=fcd800">
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
  <a href="#how-to-use">How to Use</a> |
  <a href="#documentation">Documentation</a> |
  <a href="#contribute">Contribute</a> |
  <a href="#credits">Credits</a>
</p>

## About

**BrazilCEP** is a minimalist and easy-to-use python library designed to query CEP (brazilian zip codes) data.

Its objective is to provide a common query interface to all these search services, facilitating
the integration of Python applications with these services.

Currently supports several CEP API's:

- [ViaCEP](https://viacep.com.br)
- [ApiCEP (WideNet)](https://apicep.com)

> [!NOTE]
> **BrazilCEP** is the new name of former **PyCEPCorreio** python library.
  If you want to migrate the old code to the new version, please see the [migrate](https://brazilcep.readthedocs.io/en/latest/migrate/) section in docs.

## Install

The recommended way to get BrazilCEP is to **install the latest stable release**
via [pip](http://pip-installer.org>):

```sh
pip install brazilcep
```

> [!NOTE]
> We currently support **Python 3.8+ only**. Users on older interpreter versions are urged to upgrade.

## How to Use

Making a request is very simple. Begin by importing the BrazilCEP module:

```python
>>> import brazilcep
```

Now, call the `get_address_from_cep` to query any CEP:

```python
>>> address = brazilcep.get_address_from_cep('37503-130')
```

Now, we have a *dict* object called ``address``. We can
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

## Documentation

Documentation for the current version of BrazilCEP is available from the official docs [here](https://brazilcep.readthedocs.io/en/stable).

## Contribute

See this *guideline* [here](https://github.com/mstuttgart/brazilcep/blob/develop/CONTRIBUTING.md).

## Credits

Copyright (C) 2016-2024 by Michell Stuttgart
