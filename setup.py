#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import os

from codecs import open

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            'pycep_correios',
                            '__version__.py')

about = {}
with open(version_path, 'r', 'utf-8') as f:
    exec(f.read(), about)

with open('README.rst', 'r', 'utf-8') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', 'r', 'utf-8') as history_file:
    history = history_file.read()

requirements = [
    'requests == 2.18.1',
    'Jinja2 == 2.9.6',
]

test_requirements = [
    'coveralls == 1.1',
    'flake8 == 3.3.0',
]

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme + '\n\n' + history,
    author=about['__author__'],
    author_email=about['__author_email__'],
    maintainer=about['__maintainer__'],
    maintainer_email=about['__maintainer_email__'],
    url=about['__url__'],
    download_url=about['__download_url__'],
    packages=[
        'pycep_correios',
    ],
    package_dir={'pycep_correios':
                 'pycep_correios'},
    include_package_data=True,
    install_requires=requirements,
    license=about['__license__'],
    zip_safe=False,
    keywords='correios desenvolvimento busca endereco cep',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: Portuguese',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)
