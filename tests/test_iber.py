import unittest

from requests import Session
from requests_mock import Adapter

from oligo import Iber
from oligo.exception import LoginException, ResponseException


class TestIber(unittest.TestCase):

    def setUp(self):
        self.adapter = Adapter()

        self.session = Session()
        self.session.mount('https://', self.adapter)

        self.instance = Iber(self.session)

    def test_instance(self):
        self.assertIsInstance(self.instance, Iber)

    def test_login(self):
        self.adapter.register_uri('POST',
                                  'https://www.i-de.es/consumidores/rest/loginNew/login',
                                  text='{"success":"true"}')
        self.instance.login("user", "password", self.session)

    def test_login_failed(self):
        self.adapter.register_uri('POST',
                                  'https://www.i-de.es/consumidores/rest/loginNew/login',
                                  text='{"success":"false"}')
        self.assertRaises(LoginException, self.instance.login, "user", "password", self.session)

    def test_login_failed_by_status_code(self):
        self.adapter.register_uri('POST',
                                  'https://www.i-de.es/consumidores/rest/loginNew/login',
                                  status_code=500)
        self.assertRaises(ResponseException, self.instance.login, "user", "password", self.session)


if __name__ == '__main__':
    unittest.main()
