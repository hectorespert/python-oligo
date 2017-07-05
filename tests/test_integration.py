import unittest

from oligo import iber


class TestIberIt(unittest.TestCase):

    def test_integration(self):
        instance = iber.Iber()
        self.assertIsInstance(instance, iber.Iber)

if __name__ == '__main__':
    unittest.main()