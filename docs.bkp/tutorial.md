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

## Timeout

BrazilCEP also supports set a request timeout. Use the timeout option. The default timeout is 5 seconds:

```python
from brazilcep import get_address_from_cep

# set timeout to 10 seconds
get_address_from_cep('37503-130', timeout=10)

```

## Proxy

BrazilCEP also supports proxy setings following *requests* pattern. For more details,
please official *requests* doc [here](https://requests.readthedocs.io/en/latest/user/advanced/#proxies).

```python
from brazilcep import get_address_from_cep

proxies = {
    'https': "00.00.000.000", 
    'http': '00.00.000.000',
}

# set proxies
get_address_from_cep('37503-130', proxies=proxies)

```

## Unsing differents API's

!!! note

    BrazilCEP was developed to integrate on-demand queries into web pages.
    Querying CEP in bulk through scripts or any other means is not recommended.

!!! info

    BrazilCEP is not responsible for the functioning, availability and support of any of these query API's. All of them are provided by third parties, and
    this library just provides a handy way to centralize the CEP search on these services.

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
