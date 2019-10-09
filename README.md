# python-oligo

Obtiene datos del contador inteligente en la red de iberdrola distribución

Instalación:

```
pip install oligo
```

Ejemplo, consultar consumo actual:

```python
from oligo import Iber

connection = Iber()
connection.login("user", "password")

watt = connection.watthourmeter()
print(watt)
```


Ejemplo, consultar estado ICP interno:

```python
from oligo import Iber
connection = Iber()
connection.login("user", "password")
watt = connection.icpstatus()
print(watt)
```
