import unittest

from oligo import iber
from os import environ


class TestIberIt(unittest.TestCase):

    def test_integration(self):
        user = environ.get("user", "asdfg")
        pwd = environ.get("password", "asddfg")

        instance = iber.Iber()
        self.assertIsInstance(instance, iber.Iber)
        instance.login(user, pwd)




if __name__ == '__main__':
    unittest.main()