PyCEP Correios
=============

[![Build Status](https://travis-ci.org/mstuttgart/pycep-correios.svg?branch=master)](https://travis-ci.org/mstuttgart/pycep-correios)
[![Coverage Status](https://coveralls.io/repos/github/mstuttgart/pycep-correios/badge.svg?branch=master)](https://coveralls.io/github/mstuttgart/pycep-correios?branch=master)
[![Code Health](https://landscape.io/github/mstuttgart/pycep-correios/master/landscape.svg)](https://landscape.io/github/mstuttgart/pycep-correios/master)
[![PyPI](https://img.shields.io/pypi/v/pycep-correios.svg)](https://pypi.python.org/pypi/pycep-correios)
[![PyPI](https://img.shields.io/pypi/pyversions/pycep-correios.svg)](https://pypi.python.org/pypi/pycep-correios)
[![PyPI](https://img.shields.io/pypi/l/pycep-correios.svg)](https://github.com/mstuttgart/pycep-correios/blob/master/LICENSE)

O PyCEP Correios faz uso do webservice dos correios para efetuar a busca de um dado CEP fornecido pelo usuário. O retorno dessa consulta é o endereço pertencente ao CEP.

### Instalação
O PyCEP Correios pode ser facilmente instalado com o comando a seguir:

```
pip3 install pycep-correios
```

### Como usar

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios. Não importa se o CEP fornecido possui hífen ou ponto. O PyCEPCorreios trata a entrada garantindo uma entrada válida para o *webservice* dos Correioss.
Veja os exemplos a seguir:

```python
from pycep_correios.correios import Correios

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

### Créditos

<<<<<<< 6f61a6369d43b4ec3fcfefa050a6e3d1a1405d5b
Copyright (C) 2015-2017 por Michell Stuttgart Faria
=======
Copyright (C) 2016 por Michell Stuttgart Faria
>>>>>>> Update README.md
