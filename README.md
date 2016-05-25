# PyCEP Correios
[![Build Status](https://travis-ci.org/mstuttgart/pycep-correios.svg?branch=master)](https://travis-ci.org/mstuttgart/pycep-correios)
[![Coverage Status](https://coveralls.io/repos/github/mstuttgart/pycep-correios/badge.svg?branch=master)]
(https://coveralls.io/github/mstuttgart/pycep-correios?branch=master)
[![Code Health](https://landscape.io/github/mstuttgart/pycep-correios/master/landscape.svg?style=flat)]
(https://landscape.io/github/mstuttgart/pycep-correios/master)
[![PyPI](https://img.shields.io/pypi/v/pycep-correios.svg)](https://pypi.python.org/pypi/pycep-correios)
[![PyPI](https://img.shields.io/pypi/dm/pycep-correios.svg)](https://pypi.python.org/pypi/pycep-correios)
[![PyPI](https://img.shields.io/pypi/pyversions/pycep-correios.svg)](https://pypi.python.org/pypi/pycep-correios)
[![PyPI](https://img.shields.io/pypi/l/pycep-correios.svg)](https://github.com/mstuttgart/pycep-correios/blob/master/LICENSE)

O PyCEP Correios faz uso do webservice dos correios para efetuar a busca de um dado CEP fornecido pelo usuário. O retorno dessa consulta é o endereço pertencente ao CEP.

## Instalação
O PyCEP Correios pode ser facilmente instalado com o comando a seguir:
```
sudo pip install pycep-correios
```

## Como usar

<pre lang="python"><code>
from pycep_correios.pycep_correios import PyCEPCorreios

obj = PyCEPCorreios()
endereco = obj.get_cep('37.503-130')

print endereco['rua']
print endereco['bairro']
print endereco['cidade']
print endereco['complemento']
print endereco['uf']
print endereco['outro']

</code></pre>
