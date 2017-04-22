PyCEP Correios
=============

[![Travis branch](https://img.shields.io/travis/mstuttgart/pycep-correios/develop.svg?style=flat-square)](https://travis-ci.org/mstuttgart/pycep-correios)
[![Coveralls branch](https://img.shields.io/coveralls/mstuttgart/pycep-correios/develop.svg?style=flat-square)](https://coveralls.io/github/mstuttgart/pycep-correios?branch=develop)
[![Code Health](https://landscape.io/github/mstuttgart/pycep-correios/develop/landscape.svg?style=flat-square)](https://landscape.io/github/mstuttgart/pycep-correios/develop)
[![PyPI](https://img.shields.io/pypi/v/pycep-correios.svg?style=flat-square)](https://pypi.python.org/pypi/pycep-correios)
[![PyPI](https://img.shields.io/pypi/pyversions/pycep-correios.svg?style=flat-square)](https://pypi.python.org/pypi/pycep-correios)
[![PyPI](https://img.shields.io/pypi/l/pycep-correios.svg?style=flat-square)](https://github.com/mstuttgart/pycep-correios/blob/develop/LICENSE)
[![Documentation Status](https://readthedocs.org/projects/pycep-correios/badge/?version=latest)](http://pycep-correios.readthedocs.io/pt/latest/?badge=latest)


O PyCEP Correios faz uso do webservice dos correios para efetuar a busca de um dado CEP fornecido pelo usuário. O retorno dessa consulta é o endereço pertencente ao CEP.

### Instalação
O PyCEP Correios pode ser facilmente instalado com o comando a seguir:

```
pip3 install pycep-correios
```

### Como usar

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios. Não importa se o CEP fornecido possui hífen ou ponto. O PyCEPCorreios trata a entrada garantindo uma entrada válida para o *webservice* dos Correios.
Veja os exemplos a seguir:

```python
from pycep_correios.correios import Correios
from pycep_correios.correios_exceptions import CorreiosCEPInvalidCEPException

# Tambem pode ser usado .get_cep('37503130')
endereco = Correios.get_cep('37503130')

print(endereco['rua'])
print(endereco['bairro'])
print(endereco['cidade'])
print(endereco['complemento'])
print(endereco['uf'])
print(endereco['outro'])

# Terceiro exemplo, usando o mesmo cep usado anteriormente, porém com hífen e ponto.
endereco = Correios.get_cep('37.503-130')

print(endereco['rua'])
print(endereco['bairro'])
print(endereco['cidade'])
print(endereco['complemento'])
print(endereco['uf'])
print(endereco['outro'])

# Quarto exemplo, enviamos um cep incorreto, com o numero de digitos inferior a 8.

try:
    endereco = Correios.get_cep('37.50-130')
except CorreiosCEPInvalidCEPException as exc:
    print(exc.message)

```

### Contribuidores

[Aldo Soares](https://github.com/Aldo774)

### Créditos

Copyright (C) 2015-2017 por Michell Stuttgart Faria
