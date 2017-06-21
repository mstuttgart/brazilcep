==========
Utilização
==========

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios. Ela foi refeita de modo a
tornar a sua utilização o mais simples possível.

Consultando CEP
---------------

A consulta de CEP é realizada através da função `consultar_cep`.

.. code:: python

    from pycep_correios

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
    >>> {
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

    from pycep_correios

    endereco = pycep_correios.consultar_cep('37.503-130')

Isso visa facilitar a utilização da PyCEPCorreios com CEPs fornecidos por outros sistemas como, por exemplo, um
formulário de endereço a ser preenchido pelo usuário. Desse modo, o CEP informado pelo usuário sempre será automaticamente formatado
para o formato aceito pelos *webservice* dos correios.

Quando consultamos um CEP com quantidade incorreto de digitos (diferente de 8)
ou que não existe, a PyCEPCorreios dispara uma exceção `CEPInvalido`:

.. code:: python

    from pycep_correios
    from pycep_correios.excecao import CEPInvalido

    try:
        endereco = pycep_correios.consultar_cep('00000000')
    except CEPInvalido as exc:
        print(exc)

Para outros tipos de exceção, como *timeout*, erro de conexão e etc, deve-se
utilizar as exceções fornecidas pela biblioteca *requests*.

Validando CEP
-------------

A validação d código de CEP pode ser feita através do comando `validar_cep`. A função retorna
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

    import pycep_correios

    meu_cep = '37.503-003'

    cep_formatado = pycep_correios.formatar_cep(meu_cep):
    print('O CEP %s esta formatado: %s' % (meu_cep, cep_formatado))
