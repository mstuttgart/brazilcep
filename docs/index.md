
<h2 align="center">
  <a href="https://pypi.org/project/brazilcep/">
    <img src="https://github.com/mstuttgart/brazilcep/assets/8174740/fb7c86c8-6261-4300-b2e0-65877084d865" width="15%">
  </a>
  <br>
      BrazilCEP
</h2>

<p align="center">

  <a href="https://github.com/mstuttgart/brazilcep/actions?query=workflow%3A%22Github+CI%22">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/mstuttgart/brazilcep/test-package.yml?color=fcd800&branch=develop">
  </a>

 <a href="https://codecov.io/gh/mstuttgart/brazilcep" > 
 <img alt="Codecov" src="https://img.shields.io/codecov/c/github/mstuttgart/brazilcep?color=fcd800">
 </a>

  <a href="https://www.codefactor.io/repository/github/mstuttgart/brazilcep">
    <img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/mstuttgart/brazilcep/develop?color=fcd800">
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

**BrazilCEP** is a minimalist and easy-to-use python library designed to query CEP (brazilian zip codes) data.

Its objective is to provide a common query interface to all these search services, facilitating the integration of Python applications with these services.

```python
>>> get_address_from_cep('37503-130')
{
    'bairro': 'str',
    'cep': 'str',
    'cidade': 'str',
    'logradouro': 'str',
    'uf': 'str',
    'complemento': 'str',
}
```

!!! tip

    **BrazilCEP** is the new name of former **PyCEPCorreio** python library.
    If you want to migrate the old code to the new version, please see the [migrate](/migrate) section.

## Features

* Cross-platform: Windows, Mac, and Linux are officially supported.
* Works with Python 3.8, 3.9, 3.10, 3.11 and 3.12.
* Currently supports several CEP API's:
  * [ViaCEP](https://viacep.com.br)
  * [ApiCEP (WideNet)](https://apicep.com)

BrazilCEP started as a personal study project and evolved into a serious and open source project that is used by many developers on a daily basis.
