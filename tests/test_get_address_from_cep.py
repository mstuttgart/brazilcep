
from pycep_correios import get_address_from_cep


def test_success(requests_mock):

    requests_mock.get('http://www.viacep.com.br/ws/37503130/json',
                      status_code=200,
                      text='{ "cep": "37503-130", "logradouro": "Rua Geraldino Campista", "complemento": "at\u00e9 214/215", "bairro": "Santo Ant\u00f4nio", "localidade": "Itajub\u00e1", "uf": "MG", "unidade": "", "ibge": "3132404", "gia": "" }')

    # Realizamos a consulta de CEP
    endereco = get_address_from_cep('37.503-130')

    assert endereco['bairro'] == 'Santo Antônio'
    assert endereco['cep'] == '37503-130'
    assert endereco['cidade'] == 'Itajubá'
    assert endereco['complemento'] == 'até 214/215'
    assert endereco['logradouro'] == 'Rua Geraldino Campista'
    assert endereco['uf'] == 'MG'
