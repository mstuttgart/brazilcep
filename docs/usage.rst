=====
Usage
=====

Consultar o endereço de um CEP é muito simples com o PyCEPCorreios. Não importa se o CEP fornecido possui hífen ou ponto. O PyCEPCorreios trata a entrada garantindo uma entrada válida para o *webservice* dos Correios.
    Veja os exemplos a seguir:

    .. code:: python

        from pycep_correios.correios import Correios
        from pycep_correios.correios_exceptions import CorreiosCEPInvalidCEPException

        # Tambem pode ser usado .get_cep('37503130')
        endereco = Correios.get_cep('37503130')

        print(endereco['rua'])
        print(endereco['bairro'])
        print(endereco['cidade'])
        print(endereco['complemento'])
        print(endereco['uf'])
        print(endereco['outro'])

        # Terceiro exemplo, usando o mesmo cep usado anteriormente, porém com hífen e ponto.
        endereco = Correios.get_cep('37.503-130')

        print(endereco['rua'])
        print(endereco['bairro'])
        print(endereco['cidade'])
        print(endereco['complemento'])
        print(endereco['uf'])
        print(endereco['outro'])

        # Quarto exemplo, enviamos um cep incorreto, com o numero de digitos inferior a 8.

        try:
            endereco = Correios.get_cep('37.50-130')
        except CorreiosCEPInvalidCEPException as exc:
            print(exc)
