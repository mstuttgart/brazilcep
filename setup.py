# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='pycep-correios',
    version='1.0.0',
    keywords='correios setuptools development cep',
    packages=[
        'pycep_correios',
    ],
    url='https://github.com/mstuttgart/pycep-correios',
    license='GPL v3',
    author='Michell Stuttgart',
    author_email='michellstut@gmail.com',
    description=u'Método para busca de dados de CEP no webservice dos '
                u'Correios',
    install_requires=[
        'suds',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GPL v3 License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
