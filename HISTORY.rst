=========
Histórico
=========

2.0.0 (2017-06-20)
------------------

* Atualização do código da PyCEPCorreios, deixando-a mais facil de ser utilizada
* Remoção das exceções antigas, deixando apenas a Exceção padrão da lib
* Remoção da classe PyCEPCorreios
* Alteração dos *imports* da lib para facilitar seu uso e diminuir tamanho dos *imports*
* Adicionado documentação com Sphinx
* Adicionado testes com TOX
* Adicionado método de validação de CEP e formatação de CEP

1.1.7 (2017-05-09)
------------------

* [FIX] Corrigido erro `jinja2.exceptions.TemplateNotFound: consultacep.xml`
* [FIX] Erro durante instalação da PyCEPCorreios via pip
* [FIX] Atualizado código de exemplo no README.rst
* [FIX] Atualizado exemplos na documentação

1.1.6 (2017-05-08)
------------------

* [FIX] Correção de bug durante instalação. #15
* [FIX] Correção de template xml ausente no pacote do modulo
* [FIX] Melhorias gerais no código e correções de bugs

1.1.1 (2017-02-08)
------------------

* Melhorias gerais no código
* XML schema utilizando Jinja2

1.0.1 (2016-08-03)
------------------

* Simplificação da classes Exceptions
* Organização do código de teste
* Utilização do mock para test

1.0.0 (2016-07-31)
------------------

* API migrada para Python 3. Python 2.7 não será mais suportado
* Substituição da lib *suds* pela lib *requests* para realizar as requisições

0.0.2 (2016-05-09)
------------------

* `setup.py` com número de versão atualizado e dependência corrigidas.

0.0.1 (2016-05-05)
------------------

* Versão inicial.
* Permite busca no webservice dos correios dos dados de um CEP fornecido.
