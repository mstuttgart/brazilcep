PyCEP Correios
=============

[![Build Status](https://travis-ci.org/mstuttgart/pycep-correios.svg?branch=master)](https://travis-ci.org/mstuttgart/pycep-correios)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/cce2722b3d5648d283d913b26fe12618)](https://www.codacy.com/app/michellstut/pycep-correios?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mstuttgart/pycep-correios&amp;utm_campaign=Badge_Coverage)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/cce2722b3d5648d283d913b26fe12618)](https://www.codacy.com/app/michellstut/pycep-correios?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=mstuttgart/pycep-correios&amp;utm_campaign=Badge_Grade)
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

### Contribuidores

[Aldo Soares](https://github.com/Aldo774)

### Créditos

Copyright (C) 2016 por Michell Stuttgart Faria
