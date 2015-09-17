# PyCEP Correios
[![Build Status](https://travis-ci.org/mstuttgart/correios-busca-cep.svg?branch=develop)](https://travis-ci.org/mstuttgart/correios-busca-cep)

## Sobre
O PyCEP Correios faz uso do webservice dos correios para efetuar a busca de um dado CEP fornecido pelo usuário. O retorno dessa consulta é o endereço pertencente ao CEP.

## Como usar

<pre lang="python"><code>
from pycep_correios.pycep_correios import PyCEPCorreios

obj = PyCEPCorreios()
endereco = get_cep('37.503-130')

print endereco['rua']
print endereco['bairro']
print endereco['cidade']
print endereco['complemento']
print endereco['uf']
print endereco['outro']

</code></pre>

## Dependências
O PyCEP Correios utilizada o módulo python 'suds' para envio e recebimento de 
dados do webservice. Você pode instalá-lo usando o *pip*.

`pip install suds`

Futuramente pretendo realizar a comunicação com webservice utilizando a biblioteca urllib,
de modo a tornar o PyCEP Correios livre de dependências externas.
