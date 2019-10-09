import unittest

from oligo import Iber


class TestIber(unittest.TestCase):

    def test_instance(self):
        instance = Iber()
        self.assertIsInstance(instance, Iber)


if __name__ == '__main__':
    unittest.main()
