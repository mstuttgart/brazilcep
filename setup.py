#!/usr/bin/env python
from codecs import open

from setuptools import setup

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

with open('requirements.txt', 'r') as requirements_file:
    requirements = requirements_file.read()

setup(
    name='pycep_correios',
    version='5.0.0',
    description='API para consulta de CEPs',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Michell Stuttgart Faria',
    author_email='michellstut@gmail.com',
    maintainer='Michell Stuttgart Faria',
    maintainer_email='michellstut@gmail.com',
    url='https://github.com/mstuttgart/pycep-correios',
    download_url='https://github.com/mstuttgart/pycep-correios',
    packages=[
        'pycep_correios',
    ],
    package_dir={
        'pycep_correios': 'pycep_correios',
    },
    include_package_data=True,
    install_requires=requirements,
    license='MIT License',
    zip_safe=False,
    keywords='correios viacep apicep cep',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: Portuguese',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    test_suite='tests',
)
