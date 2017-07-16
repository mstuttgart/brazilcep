==========
Utilização
==========

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios. Ela foi refeita de modo a
tornar a sua utilização o mais simples possível.

Consultando CEP
---------------

A consulta de CEP é realizada através da função `consultar_cep`.

.. code:: python

    import pycep_correios

    endereco = pycep_correios.consultar_cep('37503130')

    print(endereco['end'])
    print(endereco['bairro'])
    print(endereco['cidade'])
    print(endereco['complemento'])
    print(endereco['complemento2'])
    print(endereco['uf'])
    print(endereco['cep'])

A variavel `endereco` recebe um `dict` contendo os dados do endereço relativo
ao CEP e possui os seguintes valores:

* **end**: corresponde ao logradouro do endereço do CEP
* **bairro**: bairro referente ao CEP pesquisado
* **cidade**: cidade referente ao CEP pesquisado
* **complemento**: complemento referente ao CEP
* **complemento2**: semelhante ao `complemento`, pode indicar, por exemplo, o intervalo de números de residências ao qual o CEP pertence.
* **uf**: a sigla do estado (`SP` para São Paulo, `MG` para Minas Gerais e etc) ao qual o CEP representa
* **cep**: o CEP consultado

Por exemplo, a busca do endereço do cep `37503130` nos retorna os seguintes dados:

.. code:: python

    >>> print(endereco)
    {
        'bairro': 'Santo Antônio',
        'cep': '37503130',
        'cidade': 'Itajubá',
        'end': 'Rua Geraldino Campista',
        'id': '0',
        'uf': 'MG',
        'complemento': '',
        'complemento2': '- até 214/215',
    }

O comando tambem aceita números de CEP contendo pontos e/ou hífen. Como por exemplo:

.. code:: python

    import pycep_correios

    endereco = pycep_correios.consultar_cep('37.503-130')

Isso visa facilitar a utilização da PyCEPCorreios com CEPs fornecidos por outros sistemas como, por exemplo, um
formulário de endereço a ser preenchido pelo usuário. Desse modo, o CEP informado pelo usuário sempre será automaticamente formatado para o formato aceito pelos *webservice* dos correios.

Quando consultamos um CEP com quantidade incorreto de digitos (diferente de 8)
ou que não existe, a PyCEPCorreios dispara uma exceção `CEPInvalido`. 

A partir da versão 2.2.0, a PyCEPCorreios trouxe novos tipos de exceções, de modo a tornar a utilização da API mais robusta. A novas exceções são *Timout*, *FalhaNaConexao*, *MultiploRedirecionamento*. Todas essas exceções derivam da nova exceção base *ExcecaoPyCEPCorreios*:

.. code:: python

    from pycep_correios import consultar_cep
    from pycep_correios.excecoes import (CEPInvalido,
                                         ExcecaoPyCEPCorreios,
                                         Timeout,
                                         MultiploRedirecionamento,
                                         FalhaNaConexao)

    try:        
        endereco = pycep_correios.consultar_cep('00000000')
        
    except Timeout as exc:
        print(exec)
        
    except FalhaNaConexao as exc:
        print(exc)
        
    except MultiploRedirecionamento as exc:
        print(exc)
        
    except CEPInvalido as exc:
        print(exc)
        
    except ExcecaoPyCEPCorreios as exc:
        print(exc)

Também podemos escolher se desejamos que a consulta seja realizada no *webservice* de homologação ou produção dos Correios.
Isso pode ser útil quando estamos utilizando a PyCEPCorreios em ambiente de desenvolvimento.

Para realizar a consulta utilizando ambiente basta passar a constante `HOMOLOGACAO` como
parâmetro para o método.

.. code:: python

    from pycep_correios import consultar_cep
    from pycep_correios import HOMOLOGACAO, PRODUCAO

    # Realizando a consulta em ambiente de homologação
    endereco = consultar_cep(cep='37503130', ambiente=HOMOLOGACAO)

    # Realizando a consulta em ambiente de producao
    endereco = consultar_cep(cep='37503130', ambiente=PRODUCAO)

O valor *default* do parâmetro `ambiente` é `PRODUCAO`. Sendo assim, no caso de consultas utilizando o ambiente de produção,
informar o valor `ambiente=PRODUCAO` torna-se facultativo.

**NOTA**: Caso seja informado um valor diferente de `HOMOLOGACAO` ou `PRODUCAO` no parâmetro `ambiente`, uma
exceção do tipo `KeyError` será lançada.

Validando CEP
-------------

A validação de código de CEP pode ser feita através do comando `validar_cep`. A função retorna
`True` se a estrutura do CEP for válida e `False`, caso contrário.

.. code:: python

    import pycep_correios

    meu_cep = '37.503-003'

    if pycep_correios.validar_cep(meu_cep):
        print('O CEP %s é valido!!' % meu_cep)
    else:
        print('Ops!! O CEP %s não é valido!!' % meu_cep)

A função também aceita CEPs contendo pontuação como, por exemplo, `37.503-003`.

Formatando CEP
--------------

A funcao `formatar_cep` recebe uma string contendo o CEP, com pontos e hífens e
simplesmente os remove. É utilizada internamente pelo comando `consultar_cep`.

.. code:: python

    from pycep_correios import formatar_cep

    meu_cep = '37.503-003'

    try:
        cep_formatado = formatar_cep(meu_cep)
        print('O CEP %s esta formatado: %s' % (meu_cep, cep_formatado))
    except ValueError as exc:
        print('Erro ao formatar CEP: %s' % exc)
