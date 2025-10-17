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

✨ **Simple and Intuitive API** - Easy-to-use interface for CEP queries

🚀 **Async/Await Support** - Full support for asynchronous operations

🔄 **Multiple Web Services** - Support for ViaCEP, ApiCEP, and OpenCEP

⚡ **Fast and Lightweight** - Minimal dependencies and optimized performance

🛡️ **Type Hints** - Full type annotation support for better IDE experience

🔧 **Customizable** - Configure timeout, proxies, and preferred web service

📦 **Well Tested** - Comprehensive test coverage

## Installation

BrazilCEP requires Python 3.9 or higher.

Install using [pip](https://pip.pypa.io/):

```bash
pip install brazilcep
```

Or using [poetry](https://python-poetry.org/):

```bash
poetry add brazilcep
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

### Configuring Timeout

Set a custom timeout for requests (default is 5 seconds):

```python
# Set timeout to 10 seconds
address = get_address_from_cep('37503-130', timeout=10)
```

### Using Proxies

Configure proxy settings for requests:

```python
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}

address = get_address_from_cep('37503-130', proxies=proxies)
```

### Handling Exceptions

```python
from brazilcep import get_address_from_cep, exceptions

try:
    address = get_address_from_cep('00000-000')
except exceptions.CEPNotFound:
    print('CEP not found!')
except exceptions.InvalidCEP:
    print('Invalid CEP format!')
except exceptions.ConnectionError:
    print('Connection error!')
except exceptions.Timeout:
    print('Request timeout!')
except exceptions.BrazilCEPException as e:
    print(f'An error occurred: {e}')
```

### Complete Async Example

```python
import asyncio
from brazilcep import async_get_address_from_cep, WebService, exceptions

async def fetch_multiple_ceps():
    """Fetch multiple CEPs concurrently."""
    ceps = ['37503-130', '01310-100', '20040-020']

    tasks = [
        async_get_address_from_cep(cep, webservice=WebService.OPENCEP)
        for cep in ceps
    ]

    try:
        addresses = await asyncio.gather(*tasks)
        for cep, address in zip(ceps, addresses):
            print(f"\nCEP {cep}:")
            print(f"  Street: {address['street']}")
            print(f"  City: {address['city']}/{address['uf']}")
    except exceptions.BrazilCEPException as e:
        print(f"Error fetching addresses: {e}")

asyncio.run(fetch_multiple_ceps())
```

## Supported Web Services

| Service | Website | Status | Rate Limit |
|---------|---------|--------|------------|
| [OpenCEP](https://opencep.com) | https://opencep.com | ✅ Active | Yes |
| [ViaCEP](https://viacep.com.br) | https://viacep.com.br | ✅ Active | Yes |
| [ApiCEP](https://apicep.com) | https://apicep.com | ✅ Active | Yes |

> [!IMPORTANT]
> BrazilCEP does not guarantee the availability or support of any third-party query APIs. This library serves as a convenient interface for accessing these services. Please check each service's terms of use and rate limits.

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

### Development Setup

```bash
# Clone the repository
git clone https://github.com/mstuttgart/brazilcep.git
cd brazilcep

# Install dependencies
make setup

# Run tests
make test

# Run linting
make lint

# Run all checks
make check
```

## About CEP

**CEP** (Código de Endereçamento Postal) or **Postal Address Code** is the Brazilian postal code system created, maintained, and organized by Correios do Brasil (Brazilian Post Office). It consists of eight digits and helps streamline address organization and delivery of mail and packages across Brazil.

## Migration from PyCEPCorreios

BrazilCEP is the successor to PyCEPCorreios. To migrate your code:

**Old (PyCEPCorreios):**
```python
from pycepcorreios import get_address_from_cep
```

**New (BrazilCEP):**
```python
from brazilcep import get_address_from_cep
```

For detailed migration instructions, see the [migration guide](https://brazilcep.readthedocs.io/api.html#migrate-from-pycepcorreios).

## License

BrazilCEP is released under the [MIT License](https://github.com/mstuttgart/brazilcep/blob/main/LICENSE).

## Credits

Created and maintained by [Michell Stuttgart](https://github.com/mstuttgart).

## Support

- 📧 Issues: [GitHub Issues](https://github.com/mstuttgart/brazilcep/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/mstuttgart/brazilcep/discussions)
- 📖 Documentation: [ReadTheDocs](https://brazilcep.readthedocs.io/)

---

<p align="center">
  Made with ❤️ in Brazil
</p>
