# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='pycep-correios',
    version='1.1.5',
    keywords='correios development cep',
    packages=find_packages(exclude=['*test*']),
    zip_safe=False,
    url='https://github.com/mstuttgart/pycep-correios',
    license='MIT License',
    author='Michell Stuttgart',
    author_email='michellstut@gmail.com',
    description='Método para busca de dados de CEP no webservice dos Correios',
    long_description=open('README.md', 'r').read(),
    package_data={
        'pycep-correios': ['templates/*xml']
    },
    include_package_data=True,
    install_requires=[
        'requests >= 2.10.0',
        'Jinja2 >= 2.8',
    ],
    test_suite='test',
    tests_require=[
        'coverage',
        'coveralls',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
