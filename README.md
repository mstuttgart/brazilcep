
<p align="center">
  <a href="https://pypi.org/project/pycep-correios/">
    <img src="https://raw.githubusercontent.com/mstuttgart/pycep-correios/develop/.img/logo.jpg" width="30%">
  </a>
  <h3 align="center">PyCEPCorreios</h3>
  <h4 align="center">API para busca de CEP integrado ao serviços dos Correios, ViaCEP e ApiCEP (WideNet)</h4>
</p>

<p align="center">
  <a href="https://github.com/mstuttgart/pycep-correios/actions?query=workflow%3A%22Github+CI%22">
    <img src="https://img.shields.io/github/workflow/status/mstuttgart/pycep-correios/Github%20CI/develop?label=Github%20CI&logo=Github&style=flat-square" alt="Version">
  </a>
  <a href="https://coveralls.io/github/mstuttgart/pycep-correios">
    <img alt="Coveralls github" src="https://img.shields.io/coveralls/github/mstuttgart/pycep-correios?style=flat-square">
  </a>
  <a href="https://codeclimate.com/github/mstuttgart/pycep-correios">
      <img alt="Code Climate maintainability" src="https://img.shields.io/codeclimate/maintainability/mstuttgart/pycep-correios.svg?style=flat-square">
  </a>
  <a href="https://pypi.org/project/pycep-correios">
      <img src="https://img.shields.io/pypi/v/pycep-correios.svg?style=flat-square" alt="Ratings">
  </a>
  <a href="https://pypi.org/project/pycep-correios/">
      <img src="https://img.shields.io/pypi/pyversions/pycep-correios.svg?style=flat-square" alt="Version">
  </a>
</p>

<p align="center">
  <a href="#instalação">Instalação</a> |
  <a href="#como-usar">Como Usar</a> |
  <a href="#como-contribuir">Como Contribuir</a> |
  <a href="#créditos">Créditos</a>
</p>


## Instalação

A PyCEPCorreios pode ser facilmente instalada com o comando a seguir:

```
pip install pycep-correios
```

Atualmente, a PyCEPCorreios possui suporte para Python 3.5+.

## Como usar

*A PyCEPCorreios foi desenvolvida para integração de consultas sob demandas em páginas web. A consulta de CEPs em massa através de *scripts* ou qualquer outros meios não é recomendada.*

A PyCEPCorreios utiliza por padrão de consulta a API provida pelo serviço [ApiCEP](https://apicep.com/). Para utilização de outros serviços, devemos indica o serviço desejado ao chamar a função `get_address_from_cep`. O CEP sempre deve ser uma *string* e pode ou não conter pontuação.

### Exemplo de consulta ao serviço *ApiCEP* (default):


```python
from pycep_correios import get_address_from_cep, WebService

address = get_address_from_cep('37503-130', webservice=WebService.APICEP)
```

### Exemplo de consulta ao serviço *ViaCEP*:


```python
from pycep_correios import get_address_from_cep, WebService

address = get_address_from_cep('37503-130', webservice=WebService.VIACEP)
```

### Exemplo de consulta ao serviço dos *Correios*:

```python
from pycep_correios import get_address_from_cep, WebService

address = get_address_from_cep('37503-130', webservice=WebService.CORREIOS)
```

**Obs.:** O serviço de busca de CEP dos Correios é parte integrante do serviço SIGEPWeb e para uso do mesmo é necessário ter contrato com os Correios, conforme indicado no capítulo *Introdução* presente no [manual de integração do serviço](http://www.corporativo.correios.com.br/encomendas/sigepweb/doc/Manual_de_Implementacao_do_Web_Service_SIGEP_WEB.pdf).

### Retorno e Exceptions

Independente do serviço escolhido, o formato de resposta sempre será um objeto `dict` contendo as seguintes chaves:

```python
{
    'bairro': 'str',
    'cep': 'str',
    'cidade': 'str',
    'logradouro': 'str',
    'uf': 'str',
    'complemento': 'str',
}
```

A PyCEPCorreios tambem dá suporte a um grupo de *exceptions* que podem ser utilizadas para tratamento de quaisquer erros que ocorram durante o processo de consulta.

```python

from pycep_correios import get_address_from_cep, WebService, exceptions

try:

    address = get_address_from_cep('37503-130', webservice=WebService.APICEP)

except exceptions.InvalidCEP as eic:
    print(eic)

except exceptions.CEPNotFound as ecnf:
    print(ecnf)

except exceptions.ConnectionError as errc:
    print(errc)

except exceptions.Timeout as errt:
    print(errt)

except exceptions.HTTPError as errh:
    print(errh)

except exceptions.BaseException as e:
    print(e)

```

## Como contribuir

Deseja participar do desenvolvimento da PyCEPCorreios? Veja a *guideline* de contribuição [aqui](https://github.com/mstuttgart/pycep-correios/blob/develop/CONTRIBUTING.md).

## Créditos

Copyright (C) 2016-2022 por Michell Stuttgart
