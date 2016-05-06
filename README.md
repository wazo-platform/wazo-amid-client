# xivo-amid-client

[![Build Status](https://travis-ci.org/xivo-pbx/xivo-amid-client.svg?branch=master)](https://travis-ci.org/xivo-pbx/xivo-amid-client)

A python library to connect to xivo-amid.

Usage:

```python
from xivo_amid_client import Client

c = Client('localhost', port=9491, version='1.0', timeout=3, token='valid-token')

results = c.action('QueueSummary')
results = c.action('DBGet', {'Family': 'test', 'Key': 'variable'})
```


## How to implement a new command

Someone trying to implement a new command to the client would have to implement
a new class, sub-classing the RESTCommand (available in
xivo-lib-rest-client). The new class must be in the setup.py in the entry points
under amid_client.commands. The name of the entry point is used as the handle on
the client. For example, if your new entry point entry looks like this:

```python
entry_points={
    'amid_client.commands': [
        'foo = package.to.foo:FooCommand'
    ]
}
```

then your command will be accessible from the client like this:

```python
c = Client(...)

c.foo.bar()  # bar is a method of the FooCommand class
```


Running unit tests
------------------

```
apt-get install libpq-dev python-dev libffi-dev libyaml-dev
pip install tox
tox --recreate -e py27
```
