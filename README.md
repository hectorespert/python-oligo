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

#### Obtener el consumo horario durante un periodo

```python
from oligo import Iber
from datetime import date, timedelta
    
connection = Iber()
connection.login("user", "password")

from_date = date.today() - timedelta(days=7)
until_date = date.today() - timedelta(days=1)

consumo = connection.consumption(from_date, until_date)

print(consumo[:10])
```

Los datos son el consumo por hora en Watt-horas. En este caso tendremos los
dato de una semana, que son 7 por 24, 168 valores. Si sumamos y dividimos
por 1000, tenemos el consumo de una semana en kWh.

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

#### Retrieve the hourly consumption during a time period

```python
from oligo import Iber
from datetime import date, timedelta
    
connection = Iber()
connection.login("user", "password")

from_date = date.today() - timedelta(days=7)
until_date = date.today() - timedelta(days=1)

consumo = connection.consumption(from_date, until_date)

print(consumo[:10])
```

The values are the consumption in Watt-hours. In this case, we have the data
of one week, which are 7 times 24, 168 values. If we sum and divide by 1000,
we will have the total consumption from one week in kWh.
