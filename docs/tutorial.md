# Tutorial

First, make sure that **BrazilCEP** is [installed](/install) and updated.

Let's get started with some simple examples.

## Make a CEP request

Making a request is very simple. Begin by importing the BrazilCEP module:

```python
>>> import brazilcep
```

Now, call the `get_address_from_cep` to query any CEP:

```python
>>> address = brazilcep.get_address_from_cep('37503-130')
```

Now, we have a *dict* object called ``address``. We can
get all the address information we need from this object:

```python
 >>> address
{
    'district': 'rua abc',
    'cep': '37503130',
    'city': 'city ABC',
    'street': 'str',
    'uf': 'str',
    'complement': 'str',
}
```

The CEP always must be a string.

## Unsing differents API's

!!! note

    BrazilCEP was developed to integrate on-demand queries into web pages.
    Querying CEP in bulk through scripts or any other means is not recommended.

By default, BrazilCEP uses the API provided by the [ApiCEP](https://apicep.com) service.
To use other services, we must indicate the desired service when calling the `get_address_from_cep`
function.

Begin by importing the BrazilCEP `Webservice` class:

```python
>>> from brazilcep import get_address_from_cep, WebService
```

Now, call the `get_address_from_cep` method with `webservice` parameter.

```python
>>> get_address_from_cep('37503-130', webservice=WebService.APICEP)
{
  'district': 'rua abc',
  'cep': '37503130',
  'city': 'city ABC',
  'street': 'str',
  'uf': 'str',
  'complement': 'str',
}

```
The possible values for the `webservice` parameter are:

* `Webservice.APICEP`
* `Webservice.VIACEP`
* `Webservice.CORREIOS`

!!! info

    The Correios CEP search service is an integral part of the SIGEPWeb service and
    to use it, it is necessary to have a contract with the Correios, as indicated
    in the Introduction chapter in the service `integration manual <>`_.

## Errors and Exceptions

BrazilCEP also supports a group of exceptions that can be used to
handle any errors that occur during the query process.

```python
from brazilcep import get_address_from_cep, exceptions

try:

    get_address_from_cep('37503-130')

# when provide CEP is invalid. Wrong size or with chars that dont be numbers.
except exceptions.InvalidCEP as eic:
    print(eic)

# CEP is fine but not exist ou not found in request API's database
except exceptions.CEPNotFound as ecnf:
    print(ecnf)

# many request exception
execept exceptions.BlockedByFlood as ebbf:
    print(ebbf)

# general exceptions
except exceptions.BrazilCEPException as e:
    print(e)

```
