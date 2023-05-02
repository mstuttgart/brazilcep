# Welcome to BrazilCEP

<p align="center">
  <a href="https://pypi.org/project/brazilcep/">
    <img src="static/logo.png" width="20%">
  </a>
</p>

<p align="center">
  <a href="https://coveralls.io/github/mstuttgart/brazilcep">
    <img alt="Status" src="https://img.shields.io/pypi/status/brazilcep?style=flat-square">
  </a>
  <a href="https://pypi.org/project/brazilcep">
      <img src="https://img.shields.io/pypi/dm/brazilcep?style=flat-square" alt="Downloads">
  </a>
  <a href="https://pypi.org/project/brazilcep">
      <img src="https://img.shields.io/pypi/v/brazilcep.svg?style=flat-square" alt="Ratings">
  </a>
  <a href="https://pypi.org/project/brazilcep/">
      <img src="https://img.shields.io/pypi/pyversions/brazilcep.svg?style=flat-square" alt="Version">
  </a>
  <a href="https://coveralls.io/github/mstuttgart/brazilcep">
   <img alt="PyPI - License" src="https://img.shields.io/pypi/l/brazilcep?color=yellow&style=flat-square">
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
