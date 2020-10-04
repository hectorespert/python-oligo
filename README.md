# python-oligo

[![Build Status](https://travis-ci.org/hectorespert/python-oligo.svg?branch=master)](https://travis-ci.org/hectorespert/python-oligo)

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/hectorespert/python-oligo)

## [ES] Cliente Python (NO OFICIAL) para i-DE (Iberdrola distribución).
### Instalación:

```
pip install oligo
```
### Ejemplos:
#### Consultar consumo actual:

```python
from oligo import Iber

connection = Iber()
connection.login("user", "password")

watt = connection.watthourmeter()
print(watt)
```
#### Consultar estado ICP interno:

```python
from oligo import Iber
connection = Iber()
connection.login("user", "password")
status = connection.icpstatus()
print(status)
```
## [EN] Python client (UNOFFICIAL) for i-DE (Iberdrola distribución).
### Install:

```
pip install oligo
```
### Example:
#### Obtain current consumption:

```python
from oligo import Iber

connection = Iber()
connection.login("user", "password")

watt = connection.watthourmeter()
print(watt)
```
#### Get ICP status:

```python
from oligo import Iber
connection = Iber()
connection.login("user", "password")
status = connection.icpstatus()
print(status)
```
