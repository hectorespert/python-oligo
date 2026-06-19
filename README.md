# python-oligo

[![Python package](https://github.com/hectorespert/python-oligo/actions/workflows/test.yml/badge.svg)](https://github.com/hectorespert/python-oligo/actions/workflows/test.yml)

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/hectorespert/python-oligo)

## [ES] Cliente Python (NO OFICIAL) para i-DE (Iberdrola distribución).

> [!WARNING]
> Esta librería está en modo mantenimiento. 
> No se añadirán nuevas funcionalidades, solo se corregirán errores mientras el api web de i-DE siga funcionando de la misma manera.

### Instalación:

#### Requests support:

```
pip install oligo[requests]
```

#### Async support:

```
pip install oligo[asyncio]
```

### Autenticación

Puedes pasar el usuario y la contraseña directamente o usar las variables de entorno `I_DE_USER` e `I_DE_PASSWORD`:

```python
from oligo import Iber

connection = Iber()
connection.login("user", "password")
```

O usando variables de entorno:

```python
from oligo import Iber

connection = Iber()
connection.login()  # Lee I_DE_USER e I_DE_PASSWORD del entorno
```

### Ejemplos:

#### Consultar consumo actual (Sync):

```python
from oligo import Iber

connection = Iber()
connection.login("user", "password")

watt = connection.watthourmeter()
print(watt)
```

#### Consultar consumo actual (ASync):

```python
import asyncio
from oligo.asyncio import AsyncIber

async def main():
    connection = AsyncIber()
    await connection.login("user", "password")

    watt = await connection.watthourmeter()
    print(watt)
    await connection.close()

asyncio.run(main())
```

#### Consultar estado ICP interno (Sync):

```python
from oligo import Iber
connection = Iber()
connection.login("user", "password")
status = connection.icpstatus()
print(status)
```

#### Consultar estado ICP interno (ASync):

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

#### Obtener el consumo horario durante un periodo (Sync)

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

#### Obtener el consumo horario durante un periodo (ASync)

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

#### Obtener el consumo horario facturado durante un periodo (Sync)

```python
from oligo import Iber
from datetime import date, timedelta

connection = Iber()
connection.login("user", "password")

from_date = date.today() - timedelta(days=7)
until_date = date.today() - timedelta(days=1)

consumo = connection.billed_consumption(from_date, until_date)

print(consumo[:10])
```

#### Obtener el consumo horario facturado durante un periodo (ASync)

```python
import asyncio
from oligo.asyncio import AsyncIber
from datetime import date, timedelta

async def main():
    connection = AsyncIber()
    await connection.login("user", "password")

    from_date = date.today() - timedelta(days=7)
    until_date = date.today() - timedelta(days=1)

    consumo = await connection.billed_consumption(from_date, until_date)

    print(consumo[:10])

asyncio.run(main())
```

Los datos son el consumo por hora en Watt-horas. En este caso tendremos los
dato de una semana, que son 7 por 24, 168 valores. Si sumamos y dividimos
por 1000, tenemos el consumo de una semana en kWh.

## [EN] Python client (UNOFFICIAL) for i-DE (Iberdrola distribución).

> [!WARNING]
> This library is in maintenance mode. 
> No new features will be added, only bugs will be fixed while the i-DE web api
> continues to work in the same way.

### Authentication

You can pass the username and password directly or use the `I_DE_USER` and `I_DE_PASSWORD` environment variables:

```python
from oligo import Iber

connection = Iber()
connection.login("user", "password")
```

Or using environment variables:

```python
from oligo import Iber

connection = Iber()
connection.login()  # Reads I_DE_USER and I_DE_PASSWORD from environment
```

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

#### Retrieve the hourly billed consumption during a time period (Sync)

```python
from oligo import Iber
from datetime import date, timedelta

connection = Iber()
connection.login("user", "password")

from_date = date.today() - timedelta(days=7)
until_date = date.today() - timedelta(days=1)

consumo = connection.billed_consumption(from_date, until_date)

print(consumo[:10])
```

#### Retrieve the hourly billed consumption during a time period (Async)

```python
import asyncio
from oligo.asyncio import AsyncIber
from datetime import date, timedelta

async def main():
    connection = AsyncIber()
    await connection.login("user", "password")

    from_date = date.today() - timedelta(days=7)
    until_date = date.today() - timedelta(days=1)

    consumo = await connection.billed_consumption(from_date, until_date)

    print(consumo[:10])

asyncio.run(main())
```

The values are the consumption in Watt-hours. In this case, we have the data
of one week, which are 7 times 24, 168 values. If we sum and divide by 1000,
we will have the total consumption from one week in kWh.
