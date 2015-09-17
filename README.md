# PyCEP Correios
[![Build Status](https://travis-ci.org/mstuttgart/pycep-correios.svg?branch=develop)](https://travis-ci.org/mstuttgart/pycep-correios)

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
git clone https://github.com/mstuttgart/pycep-correios.git
cd pycep-correios/
sudo python setup.py install

