import unittest

from oligo import AIOIber


class TestIber(unittest.TestCase):

    def test_instance(self):
        instance = AIOIber()
        self.assertIsInstance(instance, AIOIber)


if __name__ == '__main__':
    unittest.main()
