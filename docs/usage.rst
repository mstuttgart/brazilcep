==========
Utilização
==========

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios. Ela foi refeita de modo a
tornar a sua utilização o mais simples possível.

Consultando CEP
---------------

A consulta de CEP é realizada através da função `get_address_from_cep`.

.. code:: python

    import pycep_correios

    endereco = pycep_correios.get_address_from_cep('37503130')

    print(endereco['logradouro'])
    print(endereco['bairro'])
    print(endereco['cidade'])
    print(endereco['complemento'])
    print(endereco['uf'])
    print(endereco['cep'])

A variavel `endereco` recebe um `dict` contendo os dados do endereço relativo
ao CEP consultado.

O comando tambem aceita números de CEP contendo pontos e/ou hífen. Como por exemplo:

.. code:: python

    import pycep_correios

    endereco = pycep_correios.get_address_from_cep('37.503-130')

Isso visa facilitar a utilização da PyCEPCorreios com CEPs fornecidos por outros sistemas como, por exemplo, um
formulário de endereço a ser preenchido pelo usuário. Desse modo, o CEP informado pelo usuário sempre será automaticamente formatado.

Quando consultamos um CEP com quantidade incorreto de digitos (diferente de 8)
ou que não existe, a PyCEPCorreios dispara uma exceção `BaseException`. 

.. code:: python

    from pycep_correios import get_address_from_cep
    from pycep_correios.exceptions import BaseException

    try:        
        endereco = pycep_correios.get_address_from_cep('00000000')
    except BaseException as exc:
        print(exec.message)

Consultando endereços
---------------------

A PyCEPCorreios tambem permite a busca de uma determinada faiza de CEPs a partir de um
endereço. Sendo assim, a partir do estado, cidade e logradouro é possível obter a faixa de CEP
correspondentes.

.. code:: python

    from pycep_correios import get_cep_from_address
    from pycep_correios.exceptions import BaseException

    try:        
        ceps = pycep_correios.get_cep_from_address(
            state='MG', city='Itajuba', street='Rua Geraldino Campista')
        
    except BaseException as exc:
        print(exec.message)

    
    print(ceps)
    >> [   
        {
            "cep": "37503-165",
            "logradouro": "Rua Geraldino Campista",
            "complemento": "de 871/872 ao fim",
            "bairro": "Santa Luzia",
            "localidade": "Itajubá",
            "uf": "MG",
            "unidade": "",
            "ibge": "3132404",
            "gia": ""
        },
        {
            "cep": "37503-130",
            "logradouro": "Rua Geraldino Campista",
            "complemento": "até 214/215",
            "bairro": "Santo Antônio",
            "localidade": "Itajubá",
            "uf": "MG",
            "unidade": "",
            "ibge": "3132404",
            "gia": ""
        },
        {
            "cep": "37503-003",
            "logradouro": "Rua Geraldino Campista",
            "complemento": "de 216/217 a 869/870",
            "bairro": "Vila Poddis",
            "localidade": "Itajubá",
            "uf": "MG",
            "unidade": "",
            "ibge": "3132404",
            "gia": ""
        }
    ]

Validando CEP
-------------

A validação de código de CEP pode ser feita através do comando `validate_cep`. A função retorna
`True` se a estrutura do CEP for válida e `False`, caso contrário.

.. code:: python

    import pycep_correios

    meu_cep = '37.503-003'

    if pycep_correios.validate_cep(meu_cep):
        print('O CEP %s é valido!!' % meu_cep)
    else:
        print('Ops!! O CEP %s não é valido!!' % meu_cep)

A função também aceita CEPs contendo pontuação como, por exemplo, `37.503-003`.

Formatando CEP
--------------

A funcao `format_cep` recebe uma string contendo o CEP, com pontos e hífens e
simplesmente os remove. É utilizada internamente pelo comando `consultar_cep`.

.. code:: python

    from pycep_correios import format_cep

    meu_cep = '37.503-003'

    try:
        cep_formatado = format_cep(meu_cep)
        print('O CEP %s esta formatado: %s' % (meu_cep, cep_formatado))
    except ValueError as exc:
        print('Erro ao formatar CEP: %s' % exc)
