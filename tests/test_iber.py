import unittest

from oligo import iber


class TestIber(unittest.TestCase):

    def test_instance(self):
        instance = iber.Iber()
        self.assertIsInstance(instance, iber.Iber)

if __name__ == '__main__':
    unittest.main()
