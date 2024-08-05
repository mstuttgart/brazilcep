# Migrate

**BrazilCEP** is the new name of former **PycepCorreios**. This page
guide you on to process of migrate old code to new version.

It's simples migrate te code and require minimal steps.

## imports

First, rename the `import` statements from:

```python title="PyCEPCorreios"
import pycepcorreios
```
to

```python title="BrazilCEP"
import brazilcep
```

## Query results

The next step, is adjust the *keys* of query returned by `get_address_from_cep` function.

The keys have simply been translated to english. Take a look on this old code:

``` python title="PyCEPCorreios"
>>> get_address_from_cep('37503-130')
{
  'bairro': 'rua abc',
  'cep': '37503130',
  'cidade': 'city ABC',
  'logradouro': 'str',
  'uf': 'str',
  'complemento': 'str',
}
```
This is the new code:

``` python title="BrazilCEP"
>>> get_address_from_cep('37503-130')
{
  'district': 'rua abc',
  'cep': '37503130',
  'city': 'city ABC',
  'street': 'str',
  'uf': 'str',
  'complement': 'str',
}
```

## Exceptions

The follow Exceptions have been removed.

```python
exceptions.ConnectionError
exceptions.Timeout
exceptions.HTTPError
exceptions.BaseException
```

Please, use the [requests](https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions) exceptions instead.

## Questions?

The best way to send question is open a issue in **BrazilCEP** issue tracker [here](https://github.com/mstuttgart/brazilcep/issues).
