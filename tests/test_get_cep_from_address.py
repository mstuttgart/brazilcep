from pycep_correios import get_cep_from_address


def test_success():

    response = [
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

    # Realizamos a consulta de enreço
    ceps = get_cep_from_address(
        state='MG', city='Itajuba', street='Rua Geraldino Campista')

    assert response == ceps
