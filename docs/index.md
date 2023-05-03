<p align="center">
  <a href="https://pypi.org/project/brazilcep/">
    <img src="https://raw.githubusercontent.com/mstuttgart/brazilcep/develop/docs/static/logo.png" width="80%">
  </a>
</p>

<p align="center">

  <a href="https://github.com/mstuttgart/brazilcep/actions?query=workflow%3A%22Github+CI%22">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/mstuttgart/brazilcep/test-package.yml?color=3771a1&branch=develop&style=flat-square">
  </a>

  <a href="https://coveralls.io/github/mstuttgart/brazilcep">
    <img alt="Coveralls github" src="https://img.shields.io/coveralls/github/mstuttgart/brazilcep?color=fcd800&style=flat-square">
  </a>

  <a href="https://www.codefactor.io/repository/github/mstuttgart/brazilcep">
    <img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/mstuttgart/brazilcep/develop?color=fcd800&style=flat-square">
  </a>

  <a href="https://pypi.org/project/brazilcep">
    <img src="https://img.shields.io/pypi/dm/brazilcep?color=fcd800&style=flat-square" alt="Downloads">
  </a>

  <a href="https://pypi.org/project/brazilcep">
    <img src="https://img.shields.io/pypi/v/brazilcep.svg?style=flat-square" alt="Ratings">
  </a>

  <a href="https://pypi.org/project/brazilcep/">
    <img src="https://img.shields.io/pypi/pyversions/brazilcep.svg?style=flat-square" alt="Version">
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
* Works with Python 3.8, 3.9, 3.10 and 3.11.
* Currently supports several CEP API's:
  * [ViaCEP](https://viacep.com.br)
  * [ApiCEP (WideNet)](https://apicep.com)
  * [Correios (SIGEPWeb)](http://www.corporativo.correios.com.br/encomendas/sigepweb/doc/Manual_de_Implementacao_do_Web_Service_SIGEP_WEB.pdf)

BrazilCEP started as a personal study project and evolved into a serious and open source project that is used by many developers on a daily basis.
