
from pycep_correios import get_address_from_cep


def test_success():

    # Realizamos a consulta de CEP
    endereco = get_address_from_cep('37.503-130')

    assert endereco['bairro'] == 'Santo Antônio'
    assert endereco['cep'] == '37503-130'
    assert endereco['cidade'] == 'Itajubá'
    assert endereco['complemento'] == 'até 214/215'
    assert endereco['logradouro'] == 'Rua Geraldino Campista'
    assert endereco['uf'] == 'MG'
