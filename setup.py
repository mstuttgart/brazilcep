#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'requests >= 2.10.0',
    'Jinja2 >= 2.8',
]

test_requirements = [
    'coverage',
    'coveralls',
    'flake8',
]

setup(
    name='pycep_correios',
    version='1.1.7',
    description='Método para busca de dados de CEP no webservice dos Correios',
    long_description=readme + '\n\n' + history,
    author='Michell Stuttgart',
    author_email='michellstut@gmail.com',
    maintainer='Michell Stuttgart',
    maintainer_email='michellstut@gmail.com',
    url='https://github.com/mstuttgart/pycep_correios',
    download_url='https://pypi.python.org/pypi/pycep-correios',
    packages=[
        'pycep_correios',
    ],
    package_dir={'pycep_correios':
                 'pycep_correios'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='correios development cep',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
