from sys import stderr

try:
    from .requests.iber import Iber
except ImportError as error:
    print(error.message, file=stderr)
