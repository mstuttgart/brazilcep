"""
PyCEPCorreios
~~~~~~~~~~~~~
PyCEPCorreios é uma API para consulta de CEP diretamente do *webservice* dos
Correios.

Uso:
   >>> import pycep_correios
   >>> endereco = pycep_correios.consultar_cep('37503130')
   >>> endereco
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

Para outros metodos suportados, veja a
documentação em https://pycep-correios.readthedocs.io.

:copyright: 2016-2017 por Michell Stuttgart Faria
:license: MIT, veja o arquivo LICENSE para mais detalhes.
"""


from .__version__ import (__title__,  # noqa: F401
                          __description__,
                          __version__,
                          __author__,
                          __author_email__,
                          __maintainer__,
                          __maintainer_email__,
                          __url__,
                          __download_url__,
                          __copyright__,
                          __license__)

from .cliente import consultar_cep, formatar_cep, validar_cep
from .cliente import HOMOLOGACAO, PRODUCAO
from .excecoes import CEPInvalido

__all__ = [
    'consultar_cep',
    'formatar_cep',
    'validar_cep',
    'CEPInvalido',
    'HOMOLOGACAO',
    'PRODUCAO',
]
