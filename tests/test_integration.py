import unittest

from oligo import iber
from os import environ
from time import sleep


class TestIberIt(unittest.TestCase):

    def test_integration(self):
        user = environ.get("user", "asdfg")
        pwd = environ.get("password", "asddfg")

        instance = iber.Iber()
        self.assertIsInstance(instance, iber.Iber)
        instance.login(user, pwd)
        sleep(2)
        watt = iber.watthourmeter()
        self.assertIsNotNone(watt)


if __name__ == '__main__':
    unittest.main()
