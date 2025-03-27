<h2 align="center">
  <a href="https://pypi.org/project/brazilcep/">
    <img src="https://github.com/mstuttgart/brazilcep/assets/8174740/fb7c86c8-6261-4300-b2e0-65877084d865" width="15%" alt="BrazilCEP Logo">
  </a>
  <br>
  BrazilCEP
</h2>

<p align="center">

  <a href="https://github.com/mstuttgart/brazilcep/actions?query=workflow%3A%22Github+CI%22">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/mstuttgart/brazilcep/test.yml?color=fcd800&branch=main">
  </a>

  <a href="https://codecov.io/gh/mstuttgart/brazilcep">
    <img alt="Codecov" src="https://img.shields.io/codecov/c/github/mstuttgart/brazilcep?color=fcd800">
  </a>

  <a href="https://brazilcep.readthedocs.io/">
    <img alt="Read the Docs" src="https://img.shields.io/readthedocs/brazilcep?color=fcd800">
  </a>

  <a href="https://pypi.org/project/brazilcep">
    <img alt="Downloads" src="https://img.shields.io/pypi/dm/brazilcep?color=fcd800">
  </a>

  <a href="https://pypi.org/project/brazilcep">
    <img alt="PyPI Version" src="https://img.shields.io/pypi/v/brazilcep.svg?color=fcd800">
  </a>

  <a href="https://pypi.org/project/brazilcep/">
    <img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/brazilcep.svg?color=fcd800">
  </a>

</p>

<p align="center">
  <a href="#about">About</a> |
  <a href="#install">Install</a> |
  <a href="#quick-start">Quick Start</a> |
  <a href="#documentation">Documentation</a> |
  <a href="#contribute">Contribute</a> |
  <a href="#credits">Credits</a>
</p>

## About

**BrazilCEP** is a minimalist and easy-to-use Python library designed to query CEP (Postal Address Code) data.

Its goal is to provide a unified query interface for multiple search services, simplifying the integration of Python applications with these services.

Currently, it supports several CEP APIs:

- [ViaCEP](https://viacep.com.br)
- [ApiCEP (WideNet)](https://apicep.com)
- [OpenCEP](https://opencep.com)

> [!NOTE]
> **BrazilCEP** is the new name of the former **PyCEPCorreio** Python library.
> To migrate your old code to the new version, refer to the [migration guide](https://brazilcep.readthedocs.io/api.html#migrate-from-pycepcorreios).

> [!TIP]
> **CEP** or **Código de Endereçamento Postal** (_Postal Address Code_) is a system of numeric codes created, maintained, and organized by _Correios do Brasil_ to streamline address organization and delivery of letters and parcels.

## Install

To install the latest stable release of BrazilCEP, use [pip](http://pip-installer.org):

```sh
pip install brazilcep
```

## Quick Start

Making a request is straightforward. Start by importing the BrazilCEP module:

```python
>>> import brazilcep
```

Next, use the `get_address_from_cep` function to query any CEP:

```python
>>> address = brazilcep.get_address_from_cep('37503-130')
```

The result is a dictionary containing the address details:

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

The CEP must always be provided as a string.

> [!TIP]
> BrazilCEP is designed for on-demand queries in web applications. Bulk querying through scripts or other means is discouraged.

> [!IMPORTANT]
> BrazilCEP does not guarantee the availability or support of any third-party query APIs. This library serves as a convenient interface for accessing these services.

#### Asynchronous Requests with BrazilCEP

BrazilCEP (version >= 7.0.0) also supports asynchronous operations , allowing you to retrieve address information for a given CEP without blocking your application. This is particularly useful for web applications or services that require high responsiveness.

To perform an asynchronous request, use the `async_get_address_from_cep` function:

```python
import asyncio
import brazilcep

async def main():
  address = await brazilcep.async_get_address_from_cep('37503-130')
  print(address)

asyncio.run(main())
```
> [!NOTE]
> This function is asynchronous and must be awaited when called.
> Ensure that your environment supports asynchronous programming before using this function.

## Documentation

Comprehensive documentation for BrazilCEP is available on [ReadTheDocs](https://brazilcep.readthedocs.io/).

## Contribute

To contribute, follow the guidelines outlined [here](https://brazilcep.readthedocs.io/contributing.html).

## Credits

Copyright (C) 2016-2024 by Michell Stuttgart
