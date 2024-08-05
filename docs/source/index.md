# **BrazilCEP**

```{toctree}
:maxdepth: 2
:hidden:
:caption: Getting started

install
tutorial
migrate
overview
```

```{toctree}
:hidden:
:caption: Development

CHANGELOG
CONTRIBUTING
License <https://raw.githubusercontent.com/mstuttgart/brazilcep/main/LICENSE>
GitHub Repository <https://github.com/mstuttgart/brazilcep>
```

<!-- ## Indices and tables -->

<!-- ```{eval-rst} -->
<!-- * :ref:`genindex` -->
<!-- * :ref:`modindex` -->
<!-- ``` -->
<p align="center">

  <a href="https://github.com/mstuttgart/brazilcep/actions?query=workflow%3A%22Github+CI%22">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/mstuttgart/brazilcep/test.yml?color=fcd800&branch=main">
  </a>

  <a href="https://pypi.org/project/brazilcep">
    <img src="https://img.shields.io/pypi/v/brazilcep.svg?" alt="Ratings">
  </a>

  <a href="https://pypi.org/project/brazilcep/">
    <img src="https://img.shields.io/pypi/pyversions/brazilcep.svg" alt="Version">
  </a>

</p>


**BrazilCEP** is a minimalist and easy-to-use python library designed to query CEP (brazilian zip codes) data.

-----------------------------

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

**BrazilCEP** is the new name of former **PyCEPCorreio** python library. If you want to migrate the old code to the new version, please see the [migrate](/migrate) section.

## Features

* Cross-platform: Windows, Mac, and Linux are officially supported.
* Works with Python 3.8, 3.9, 3.10, 3.11 and 3.12.
* Currently supports several CEP API's:
  * [ViaCEP](https://viacep.com.br)
  * [ApiCEP (WideNet)](https://apicep.com)
  * [OpenCEP](https://opencep.com/)
  * [Correios (site)](https://www2.correios.com.br/sistemas/buscacep/resultadoBuscaEndereco.cfm)

BrazilCEP started as a personal study project and evolved into a serious and open source project that is used by many developers on a daily basis.

