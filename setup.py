# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pycep_correios import __version__

setup(
    name='pycep-correios',
    version=__version__,
    keywords='correios development cep',
    packages=find_packages(exclude=['*test*']),
    zip_safe=False,
    url='https://github.com/mstuttgart/pycep-correios',
    download_url='https://pypi.python.org/pypi/pycep-correios',
    license='MIT License',
    author='Michell Stuttgart',
    author_email='michellstut@gmail.com',
    maintainer='Michell Stuttgart',
    maintainer_email='michellstut@gmail.com',
    description='Método para busca de dados de CEP no webservice dos Correios',
    long_description=open('README.rst', 'r').read(),
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
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
    ],
)
