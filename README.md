# PyCEP Correios
[![Build Status](https://travis-ci.org/mstuttgart/pycep-correios.svg?branch=master)](https://travis-ci.org/mstuttgart/pycep-correios)
[![Coverage Status](https://coveralls.io/repos/github/mstuttgart/pycep-correios/badge.svg?branch=master)]
(https://coveralls.io/github/mstuttgart/pycep-correios?branch=master)
[![Code Health](https://landscape.io/github/mstuttgart/pycep-correios/master/landscape.svg?style=flat)]
(https://landscape.io/github/mstuttgart/pycep-correios/master)
[![PyPI](https://img.shields.io/pypi/v/pycep-correios.svg?maxAge=2592000?style=plastic)]()
[![PyPI](https://img.shields.io/pypi/dm/pycep-correios.svg?maxAge=2592000?style=plastic)](https://pypi.python.org/pypi/pycep-correios/0.0.1)
[![PyPI](https://img.shields.io/pypi/pyversions/pycep-correios.svg?maxAge=2592000?style=plastic)]()
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/kefir500/ghstats/master/LICENSE)

O PyCEP Correios faz uso do webservice dos correios para efetuar a busca de um dado CEP fornecido pelo usuário. O retorno dessa consulta é o endereço pertencente ao CEP.

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

## Dependências
O PyCEP Correios as seguintes dependências para envio e recebimento de 
dados do webservice. 

* python 2.7
* suds

Instale o *suds* com:

`pip install suds`

Futuramente pretendo realizar a comunicação com *webservice* utilizando a biblioteca *urllib*,
de modo a tornar o PyCEP Correios livre de dependências externas.

## Instalação

`git clone https://github.com/mstuttgart/pycep-correios.git`

`cd pycep-correios/`

`sudo python setup.py install`

