
<h1 align="center">
  <br>
  <a href="https://pypi.org/project/pycep-correios/">
  <img src="https://raw.githubusercontent.com/mstuttgart/pycep-correios/develop/docs/_static/logo.jpg" width="30%"></a>
  <br>
  PyCEPCorreios
  <br>
</h1>

<h4 align="center">API para consulta de CEP diretamente do <i>webservice</i> dos Correios</h4>

<p align="center">
  <a href="https://travis-ci.org/mstuttgart/pycep-correios">
    <img src="https://img.shields.io/travis/mstuttgart/pycep-correios/develop.svg?style=flat-square" alt="Version">
  </a>
  <a href="https://coveralls.io/github/mstuttgart/pycep-correios?branch=develop">
    <img src="https://img.shields.io/coveralls/mstuttgart/pycep-correios/develop.svg?style=flat-square" alt="Installs">
  </a>
  <a href="https://landscape.io/github/mstuttgart/pycep-correios/develop">
      <img src="https://landscape.io/github/mstuttgart/pycep-correios/develop/landscape.svg?style=flat-square" alt="Ratings">
  </a>
  <a href="https://pypi.org/project/pycep-correios">
      <img src="https://img.shields.io/pypi/v/pycep-correios.svg?style=flat-square" alt="Ratings">
  </a>
  <a href="https://pypi.org/project/pycep-correios/">
      <img src="https://img.shields.io/pypi/pyversions/pycep-correios.svg?style=flat-square" alt="Ratings">
  </a>
</p>

<p align="center">
  <a href="#recursos">Recursos</a> |
  <a href="#documentação">Documentação</a> |
  <a href="#instalação">Instalação</a> |
  <a href="#como-usar">Como Usar</a> |
  <a href="#como-contribuir">Como Contribuir</a> |
  <a href="#créditos">Créditos</a>
</p>


## Recursos

-   Consulta de dados do endereço de um CEP
-   Formatacao de CEP
-   Validação de estrutura do CEP

## Documentação

Para mais detalhes sobre a PyCEPCorreios, por gentileza, consulte a documentação oficial:

-   Documentação online: [docs](https://pycep-correios.readthedocs.io/pt/stable/)
-   Documentação PDF: [download](https://media.readthedocs.org/pdf/pycep-correios/stable/pycep-correios.pdf)

## Instalação

O PyCEP Correios pode ser facilmente instalado com o comando a seguir:

```shell
pip install pycep-correios
```

Atualmente, a PyCEPCorreios possui suporte para Python 3.4+.

## Como usar

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios. Veja os exemplos a seguir:

```python
>>> import pycep_correios

>>> endereco = pycep_correios.consultar_cep('37503130')
>>> print(endereco)
{
    'bairro': 'Santo Antônio',
    'cep': '37503130',
    'cidade': 'Itajubá',
    'end': 'Rua Geraldino Campista',
    'uf': 'MG',
    'complemento2': '- até 214/215',
}
```

## Como contribuir

Deseja participar do desenvolvimento da PyCepCorreios? Torne-se um contribuidor do PyCEPCorreios! visite a documentação para verificar a *guideline* de contribuição:

-   Veja [aqui](https://pycep-correios.readthedocs.io/pt/stable/contributing.html).

### Aviso de *bugs*, dúvidas e sugestões

Para dúvidas, sugestões e relatórios de *bugs*, por gentileza, crie uma *issue*:

-   Issue Tracker: <https://github.com/mstuttgart/pycep-correios/issues>

### Contribuidores

Agradecimentos aos seguintes contribuidores pelo esforço de fazer a PyCEPCorreios melhor:

-   Lista de contribuidores: <https://github.com/mstuttgart/pycep-correios/graphs/contributors>

## Créditos

Copyright (C) 2016-2018 por Michell Stuttgart
