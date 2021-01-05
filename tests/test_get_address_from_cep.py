
from pycep_correios import get_address_from_cep
from pycep_correios import APICEP, VIACEP


def test_viacep_success():

    # Realizamos a consulta de CEP
    endereco = get_address_from_cep('37.503-130', server=VIACEP)

    assert endereco['bairro'] == 'Santo Antônio'
    assert endereco['cep'] == '37503-130'
    assert endereco['cidade'] == 'Itajubá'
    assert endereco['complemento'] == 'até 214/215'
    assert endereco['logradouro'] == 'Rua Geraldino Campista'
    assert endereco['uf'] == 'MG'

def test_apicep_success():

    # Realizamos a consulta de CEP
    endereco = get_address_from_cep('37.503-130', server=APICEP)

    assert endereco['bairro'] == 'Santo Antônio'
    assert endereco['cep'] == '37503-130'
    assert endereco['cidade'] == 'Itajubá'
    assert endereco['complemento'] == ''
    assert endereco['logradouro'] == 'Rua Geraldino Campista'
    assert endereco['uf'] == 'MG'
