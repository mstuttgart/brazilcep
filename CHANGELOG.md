# Changelog

## 5.0.0 (2021-01-06)

* Adiciona suporte para Python 3.8
* Adiciona integração com consulta de CEP nos webservices dos Correios
* Adiciona integração com consulta de CEP no webservice da APICEP.com
* Adiciciona novas exceptions para melhor tratamentos de erros.
* Remove deprecated methods (consulta_cep, validar_cep, formatar_cep)
* Remove deprecated exceptions (ExcecaoPyCEPCorreios, CEPInvalido, FalhaNaConexao, MultiploRedirecionamento, Timeout)
* Remove function 'get_cep_from_address', por falta de uso
* Remove documentação antiga e centraliza exemplos de uso no README
* Uso de TOX para testes em diferentes versões do Python
* Adiciona novos testes e aumenta taxa do coverage

## 4.0.4 (2020-08-18)

* Corrige "AttributeError: 'ConnectionError' object has no attribute 'message'"

## 4.0.3 (2020-06-08)

* Corrige 'get_cep_from_address' error key - thanks Hendrix Costa https://github.com/hendrixcosta
* Corrige docs

## 4.0.2 (2020-05-31)

* Corrige exemplo de uso do 'get_cep_from_address'
* Corrige "(client): KeyError exception when address not found" - thanks Patrick Ferraz https://github.com/patricksferraz
* Adiciona captura de erro com status_code=200 - thanks Bruno Mello https://github.com/bgmello

## 4.0.1 (2020-02-22)

* Corrige travis.yml deploy

## 4.0.0 (2020-02-22)

* Adiciona suporte a API do ViaCEP (https://viacep.com.br/)
* Adiciona consulta de faixa de CEPs
* Adiciona function format_cep, validate_cep
* Adiciona nova function de busca de CEP
* Adiciona suporte para Python 3.7
* Ajustes no codigo e documentação

Milestone: https://github.com/mstuttgart/pycep-correios/milestone/4

## 3.2.0 (2019-08-18)

* Remove suporte para Python 3.4: https://www.python.org/downloads/release/python-3410/
* Adiciona suporte para retorno com atributos ausentes
* Adiciona mock aos testes

## 3.1.0 (2018-11-11)

* Correção no tipo do retorno do metodo consultar_cep (por questões de compatibilidade, agora retorna um dict)
* Correção da documentação, pois as tags 'id' e 'complemento' não estão mais sendo retornadas pelo Correios.
* Atualização do README.md para uso de markdown no pypi e documentação.

## 3.0.0 (2018-10-21)

* Alteração da API de consulta para [python-zeep](https://pypi.org/project/zeep/)
* Antigas `exceptions` agora estão `deprecated`. Usar apenas `ExcecaoPyCEPCorreios`
* Atualização da documentação
* Remoção do suporte para Python 2.7

## 2.3.1 (2018-05-03)

* Corrige README.rst
* Adiciona comando para validação dpo setup.py no Makefile
* Corrige link do repositorio e donwload

## 2.3.0 (2018-05-03)

* Adiciona logging para consulta de CEP
* Adiciona documentação em inglês
* Versão requirida das libs *requests* e da *Jinja2* limitadas por baixo, para fins de compatibilidade
* Remove suporte para Python 3.3

## 2.2.0 (2017-07-16)

* Melhorias no metodo de formatar_cep, que agora passou a utilizar expressão regular para verificar se o CEP é formado por caracteres.
* A função *formatar_cep* agora passa a lançar a exceção *Value Error* quando o CEP não possui estrutura válida https://github.com/mstuttgart/pycep-correios/pull/22
* Adicionado novas exceções ExcecaoPyCEPCorreios, Timeout, MultiploRedirecionamento, FalhaNaConexao. Consultar documentacao para exemplos de utilização delas. close https://github.com/mstuttgart/pycep-correios/issues/25
* Adicionado ambientes de *Homologação* e *Producao*. Facilitando realizar consultas utilizadas para testes. close https://github.com/mstuttgart/pycep-correios/issues/24
* Melhorias na organização da API.

## 2.1.1 (2017-06-30)

* Correção de erros de unicode com python2.7

## 2.1.0 (2017-06-29)

* Adicionado suporte para Python 2.7+
* Ajustes e correções na documentação

## 2.0.0 (2017-06-20)

* Atualização do código da PyCEPCorreios, deixando-a mais facil de ser utilizada
* Remoção das exceções antigas, deixando apenas a Exceção padrão da lib
* Remoção da classe PyCEPCorreios
* Alteração dos *imports* da lib para facilitar seu uso e diminuir tamanho dos *imports*
* Adicionado documentação com Sphinx
* Adicionado testes com TOX
* Adicionado método de validação de CEP e formatação de CEP

## 1.1.7 (2017-05-09)

* Corrigido erro `jinja2.exceptions.TemplateNotFound: consultacep.xml`
* Erro durante instalação da PyCEPCorreios via pip
* Atualizado código de exemplo no README.rst
* Atualizado exemplos na documentação

## 1.1.6 (2017-05-08)

* Correção de bug durante instalação. #15
* Correção de template xml ausente no pacote do modulo
* Melhorias gerais no código e correções de bugs

## 1.1.1 (2017-02-08)

* Melhorias gerais no código
* XML schema utilizando Jinja2

## 1.0.1 (2016-08-03)

* Simplificação da classes Exceptions
* Organização do código de teste
* Utilização do mock para test

## 1.0.0 (2016-07-31)

* API migrada para Python 3. Python 2.7 não será mais suportado
* Substituição da lib *suds* pela lib *requests* para realizar as requisições

## 0.0.2 (2016-05-09)

* `setup.py` com número de versão atualizado e dependência corrigidas.

## 0.0.1 (2016-05-05)

* Versão inicial.
* Permite busca no webservice dos correios dos dados de um CEP fornecido.
