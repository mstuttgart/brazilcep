<h2 align="center">
  <a href="https://pypi.org/project/brazilcep/">
    <img src="https://github.com/mstuttgart/brazilcep/assets/8174740/fb7c86c8-6261-4300-b2e0-65877084d865" width="15%" alt="BrazilCEP Logo">
  </a>
  <br>
  BrazilCEP
</h2>

<p align="center">
  <strong>A minimalist and easy-to-use Python library for querying Brazilian CEP (Postal Address Code) data</strong>
</p>

<p align="center">

  <a href="https://github.com/mstuttgart/brazilcep/actions?query=workflow%3A%22Github+CI%22">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/mstuttgart/brazilcep/test.yml?color=fcd800&branch=main">
  </a>

  <a href="https://codecov.io/gh/mstuttgart/brazilcep">
    <img alt="Codecov" src="https://img.shields.io/codecov/c/github/mstuttgart/brazilcep?color=fcd800">
  </a>

  <a href="https://brazilcep.readthedocs.io/">
    <img alt="Read the Docs" src="https://img.shields.io/readthedocs/brazilcep?color=fcd800">
  </a>

  <a href="https://pypi.org/project/brazilcep">
    <img alt="Downloads" src="https://static.pepy.tech/badge/brazilcep">
  </a>

  <a href="https://pypi.org/project/brazilcep">
    <img alt="PyPI Version" src="https://img.shields.io/pypi/v/brazilcep.svg">
  </a>

  <a href="https://pypi.org/project/brazilcep/">
    <img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/brazilcep.svg">
  </a>

  <a href="https://github.com/mstuttgart/brazilcep/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/mstuttgart/brazilcep?color=fcd800">
  </a>

</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#usage-examples">Usage Examples</a> •
  <a href="#documentation">Documentation</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

## Features

- Easy-to-use interface for CEP queries
- Full support for asynchronous operations
- Support for **ViaCEP**, **ApiCEP**, and **OpenCEP**
- Minimal dependencies and optimized performance
- Full type annotation support for better IDE experience
- Configure timeout, proxies, and preferred web service
- Comprehensive test coverage

## About CEP

**CEP** (Código de Endereçamento Postal) or **Postal Address Code** is the Brazilian postal code system created, maintained, and organized by Correios do Brasil (Brazilian Post Office). It consists of eight digits and helps streamline address organization and delivery of mail and packages across Brazil.


## Installation

BrazilCEP requires Python 3.9 or higher.

Install using [pip](https://pip.pypa.io/):

```bash
pip install brazilcep
```

## Quick Start

### Synchronous Usage

```python
import brazilcep

# Query a CEP
address = brazilcep.get_address_from_cep('37503-130')

print(address)
# Output:
# {
#     'cep': '37503-130',
#     'street': 'Rua Geraldino Campista',
#     'district': 'Santo Antônio',
#     'city': 'Itajubá',
#     'uf': 'MG',
#     'complement': 'até 214/215'
# }
```

### Asynchronous Usage

```python
import asyncio
import brazilcep

async def main():
    address = await brazilcep.async_get_address_from_cep('37503-130')
    print(address)

asyncio.run(main())
```

## Usage Examples

### Choosing a Web Service

BrazilCEP supports multiple CEP lookup services. You can specify which one to use:

```python
from brazilcep import get_address_from_cep, WebService

# Using ViaCEP (default for backwards compatibility, but OpenCEP is now default)
address = get_address_from_cep('37503-130', webservice=WebService.VIACEP)

# Using ApiCEP
address = get_address_from_cep('37503-130', webservice=WebService.APICEP)

# Using OpenCEP (default)
address = get_address_from_cep('37503-130', webservice=WebService.OPENCEP)
```

## Response Format

All queries return a dictionary with the following structure:

```python
{
    'cep': str,        # Postal code (e.g., '37503-130')
    'street': str,     # Street name (e.g., 'Rua Geraldino Campista')
    'district': str,   # Neighborhood/district (e.g., 'Santo Antônio')
    'city': str,       # City name (e.g., 'Itajubá')
    'uf': str,         # State abbreviation (e.g., 'MG')
    'complement': str  # Additional information (may be empty)
}

```
## Supported Web Services

| Service                         | Website               | Status   | Rate Limit |
| ------------------------------- | --------------------- | -------- | ---------- |
| [OpenCEP](https://opencep.com)  | https://opencep.com   | ✅ Active | Yes        |
| [ViaCEP](https://viacep.com.br) | https://viacep.com.br | ✅ Active | Yes        |
| [ApiCEP](https://apicep.com)    | https://apicep.com    | ✅ Active | Yes        |

> [!IMPORTANT]
> BrazilCEP does not guarantee the availability or support of any third-party query APIs. This library serves as a convenient interface for accessing these services. Please check each service's terms of use and rate limits.

## Documentation

For comprehensive documentation, including advanced usage, API reference, and migration guides, visit:

📚 **[BrazilCEP Documentation](https://brazilcep.readthedocs.io/)**

### Quick Links

- [API Reference](https://brazilcep.readthedocs.io/api.html)
- [Migration from PyCEPCorreios](https://brazilcep.readthedocs.io/api.html#migrate-from-pycepcorreios)
- [Contributing Guide](https://brazilcep.readthedocs.io/contributing.html)
- [Changelog](https://github.com/mstuttgart/brazilcep/blob/main/CHANGELOG)

## Contributing

Contributions are welcome! Here's how you can help:

1. 🐛 **Report bugs** - Open an issue describing the bug
2. 💡 **Suggest features** - Share your ideas for improvements
3. 📝 **Improve documentation** - Help make the docs clearer
4. 🔧 **Submit pull requests** - Fix bugs or add features

Please read our [Contributing Guide](https://brazilcep.readthedocs.io/contributing.html) before submitting a pull request.

## License

BrazilCEP is released under the [MIT License](https://github.com/mstuttgart/brazilcep/blob/main/LICENSE).

Created and maintained by [Michell Stuttgart](https://github.com/mstuttgart).
