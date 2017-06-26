# python-oligo

Obtiene datos del contador inteligente en la red de iberdrola distribución [WIP]

Instalación:

```
pip install oligo
```

Ejemplo, consultar consumo actual:

```python
from oligo import iber

watt = iber.watthourmeter("tu_usuario", "tu_contraseña")
print(watt)
```


Ejemplo, consultar estado ICP interno:

```python
from oligo import iber

watt = iber.icpstatus("tu_usuario", "tu_contraseña")
print(watt)
```
