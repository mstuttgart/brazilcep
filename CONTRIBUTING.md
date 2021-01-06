# Como Contribuir

Contribuições são bem-vindas e muito apreciadas!

## Tipos de contribuições

Você pode contribuir de várias maneiras:

### Reportando erros

Informe erros em https://github.com/mstuttgart/pycep-correios/issues.

Se você está reportando um *bug*, por favor inclua:

* O nome e a versão do seu sistema operacional.
* Qualquer detalhe sobre sua configuração local que possa ser útil na solução de problemas.
* Etapas detalhadas para reproduzir o bug.

### Corrigindo erros

Busque na lista de *issues* por aquelas com a tag *Bug*.
Qualquer *issue* marcada com "Bug" está aberta para quem quiser corrigi-la.

### Adicionando novos recursos

Busque na lista de *issues* por aquelas com a tag *Improvement* ou *New feature*.
Qualquer *issue* marcada com esses *tags* está aberta para quem quiser implementá-la.

### Enviando Sugestões e Dúvidas

A melhor maneira de enviar sugestões e dúvidas é abrir uma *issue* em https://github.com/mstuttgart/pycep-correios/issues.

## Comece a contribuir!

Pronto para contribuir? Veja como configurar `pycep_correios` para desenvolvimento local.

1. Fork o repositório `pycep_correios` no GitHub.
2. Clone sua *branch* localmente::

> $ git clone git@github.com:your_name_here/pycep-correios.git

3. Instale sua cópia local em um *virtualenv*. Supondo que você tenha instalado o *virtualenv*, é assim que você configura a seu *fork* para o desenvolvimento local::

> cd pycep-correios

> virtualenv env -p python3

> source env/bin/activate

> pip install -r requirements-dev.txt

4. Crie uma *branch* para desenvolvimento::

> git checkout -b nome-da-sua-branch

   Agora você pode fazer suas mudanças localmente.

1. Quando terminar de fazer alterações, verifique se suas alterações passam nos testes::

> pytest

1. Confirme as suas alterações e as envie para o GitHub::

> git add .

> git commit -m "Descricao detalhada das sua alteracoes. (de preferencia em ingles)"

> git push origin nome-da-sua-branch

7. Envie um *Pull Request* para o repositório oficial da PyCEPCorreios no GitHub.

## Como criar um Pull Request

Após enviar um pedido de *Pull Request*, verifique se ele atende a essas diretrizes:

1. O pedido de *Pull Request* deve incluir testes, quando for uma nova *feature*.
2. Se o *Pull Request* adicionar funcionalidades, a documentação deve ser atualizada adicionado detalhes de uso da nova funcionalidade.
3. O pedido de *Pull Request* deve funcionar para o 3.5+.
