# python-oligo

[![Python package](https://github.com/hectorespert/python-oligo/actions/workflows/test.yml/badge.svg)](https://github.com/hectorespert/python-oligo/actions/workflows/test.yml)

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/hectorespert/python-oligo)

## Python client (UNOFFICIAL) for i-DE (Iberdrola distribución).
### Install:

```
pip install oligo
```
### Example:
#### Obtain current consumption (Sync):

```python
from oligo import Iber

connection = Iber()
connection.login("user", "password")

watt = connection.watthourmeter()
print(watt)
```
#### Obtain current consumption (ASync):

```python
import asyncio
from oligo.asyncio import AsyncIber

async def main():
    connection = AsyncIber()
    await connection.login("user", "password")

    watt = await connection.watthourmeter()
    print(watt)

asyncio.run(main())
```

#### Get ICP status (Sync):

```python
from oligo import Iber
connection = Iber()
connection.login("user", "password")
status = connection.icpstatus()
print(status)
```

#### Get ICP status (ASync):

```python
import asyncio
from oligo.asyncio import AsyncIber

async def main():
    connection = AsyncIber()
    await connection.login("user", "password")
    status = await connection.icpstatus()
    print(status)

asyncio.run(main())
```

#### Retrieve the hourly consumption during a time period (Sync)

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

#### Retrieve the hourly consumption during a time period (Async)

```python
import asyncio
from oligo.asyncio import AsyncIber
from datetime import date, timedelta

async def main():
    connection = AsyncIber()
    await connection.login("user", "password")

    from_date = date.today() - timedelta(days=7)
    until_date = date.today() - timedelta(days=1)

    consumo = await connection.consumption(from_date, until_date)

    print(consumo[:10])

asyncio.run(main())
```

The values are the consumption in Watt-hours. In this case, we have the data
of one week, which are 7 times 24, 168 values. If we sum and divide by 1000,
we will have the total consumption from one week in kWh.
