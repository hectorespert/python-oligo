import unittest

from oligo.asyncio import AsyncIber


class TestAsyncIber(unittest.TestCase):

    def test_instance(self):
        instance = AsyncIber()
        self.assertIsInstance(instance, AsyncIber)


if __name__ == '__main__':
    unittest.main()
