import warnings

import zeep
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from . import exceptions

URL = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'  # noqa


def fetch_address(cep):

    try:
        with warnings.catch_warnings():

            # Desabilitamos o warning
            warnings.simplefilter('ignore', InsecureRequestWarning)
            warnings.simplefilter('ignore', ImportWarning)

            client = zeep.Client(URL)

            address = client.service.consultaCEP(cep)

            return {
                'bairro': getattr(address, 'bairro', ''),
                'cep': getattr(address, 'cep', ''),
                'cidade': getattr(address, 'cidade', ''),
                'logradouro': getattr(address, 'end', ''),
                'uf': getattr(address, 'uf', ''),
                'complemento': getattr(address, 'complemento2', ''),
            }

    except zeep.exceptions.Fault as e:
        raise exceptions.BaseException(e)
