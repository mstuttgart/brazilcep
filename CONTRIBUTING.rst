.. highlight:: shell

============
Contribuindo
============

Contribuições são bem-vindas e muito apreciadas!

Você pode contribuir de várias maneiras:

Tipos de Contribuições
----------------------

Reportando erros
~~~~~~~~~~~~~~~~

Informe erros em https://github.com/mstuttgart/pycep-correios/issues.

Se você está reportando um *bug*, por favor inclua:

* O nome e a versão do seu sistema operacional.
* Qualquer detalhe sobre sua configuração local que possa ser útil na solução de problemas.
* Etapas detalhadas para reproduzir o bug.

Corrigindo erros
~~~~~~~~~~~~~~~~

Busque na lista de *issues* por aquelas com a tag *Bug*.
Qualquer *issue* marcada com "Bug" está aberta para quem quiser corrigí-la.

Adicionando novos recursos
~~~~~~~~~~~~~~~~~~~~~~~~~~

Busque na lista de *issues* por aquelas com a tag *Improvement* ou *New feature*.
Qualquer *issue* marcada com esses *tags* está aberta para quem quiser implementá-la.

Melhorando a documentação
~~~~~~~~~~~~~~~~~~~~~~~~~

A documentação da PyCEPCorreios sempre pode ser melhorada, seja como parte do
da documentação oficial do PyCEPCorreios, em docstrings, ou mesmo na web em postagens de blog,
artigos e etc. Então caso você tenha escrito alguma postagem sobre a PyCEPCorreios, por favor,
me avise para que a mesma seja incluída aqui como referência.

Enviar Comentários
~~~~~~~~~~~~~~~~~~

A melhor maneira de enviar comentários é abrir uma *issue* em https://github.com/mstuttgart/pycep-correios/issues.

Se você está propondo um novo recurso para PyCEPCorreios, por favor siga os seguintes passos:

* Explique em detalhes como isso funcionaria.
* Mantenha o escopo o mais simples possível, para facilitar a implementação.
* Lembre-se que este é um projeto voluntário, e que contribuições são bem-vindos :)

Começando a contribuir!
-----------------------

Pronto para contribuir? Veja como configurar `pycep_correios` para desenvolvimento local.

1. Fork o repositório `pycep_correios` no GitHub.
2. Clone sua *branch* localmente::

    $ git clone git@github.com:your_name_here/pycep-correios.git

3. Instale sua cópia local em um *virtualenv*. Supondo que você tenha instalado o *virtualenv*, é assim que você configura a seu *fork* para o desenvolvimento local::

    $ cd pycep-correios
    $ virtualenv -p python3 env
    $ pip3 install -r requirements.txt

4. Crie uma *branch* para desenvolvimento::

    $ git checkout -b nome-da-sua-branch

   Agora você pode fazer suas mudanças localmente.

5. Quando terminar de fazer alterações, verifique se suas alterações passam no *flake8* e nos testes::

    $ flake8 pycep_correios tests
    $ python setup.py test

6. Confirme as suas alterações e as envie para o GitHub::

    $ git add .
    $ git commit -m "Descricao detalhada das sua alteracoes."
    $ git push origin nome-da-sua-branch

7. Envie um *Pull Request* para o repositório oficial da PyCEPCorreios no GitHub.

Instruções de Solicitação de Pull Request
-----------------------------------------

Antes de enviar um pedido de *Pull Request*, verifique se ele atende a essas diretrizes:

1. O pedido de *Pull Request* deve incluir testes, quando for uma nova *feature*.
2. Se o *Pull Request* adicionar funcionalidades, a documentação deve ser atualizada adicionado detalhes de uso da nova funcionalidade.
3. O pedido de *Pull Request* deve funcionar para o Python 3.3, 3.4, 3.5 e 3.6. Verificar https://travis-ci.org/mstuttgart/pycep-correios/pull_requests e certifique-se de que os testes passem para todas as versões do Python suportadas.
