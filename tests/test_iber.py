import os
import unittest
from datetime import date
from unittest.mock import MagicMock, patch

from requests import Session

from oligo import Iber
from oligo.exception import LoginException, ResponseException


class TestIber(unittest.TestCase):
    def setUp(self):
        self._env_backup = {}
        for key in ("I_DE_USER", "I_DE_PASSWORD"):
            if key in os.environ:
                self._env_backup[key] = os.environ.pop(key)
        self.session = Session()
        self.instance = Iber(self.session)

    def tearDown(self):
        for key, value in self._env_backup.items():
            os.environ[key] = value

    def test_instance(self):
        self.assertIsInstance(self.instance, Iber)

    def test_login(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '{"success":"true"}'
        mock_response.json.return_value = {"success": "true"}

        with patch.object(self.session, "request", return_value=mock_response):
            self.instance.login("user", "password", self.session)

    def test_login_with_env_vars(self):
        os.environ["I_DE_USER"] = "env_user"
        os.environ["I_DE_PASSWORD"] = "env_pass"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '{"success":"true"}'
        mock_response.json.return_value = {"success": "true"}

        with patch.object(
            self.session, "request", return_value=mock_response
        ) as mock_request:
            self.instance.login(session=self.session)
            _, kwargs = mock_request.call_args
            payload = kwargs["json"]
            self.assertEqual(payload[0], "env_user")
            self.assertEqual(payload[1], "env_pass")

    def test_login_explicit_args_override_env_vars(self):
        os.environ["I_DE_USER"] = "env_user"
        os.environ["I_DE_PASSWORD"] = "env_pass"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '{"success":"true"}'
        mock_response.json.return_value = {"success": "true"}

        with patch.object(
            self.session, "request", return_value=mock_response
        ) as mock_request:
            self.instance.login("user", "password", self.session)
            _, kwargs = mock_request.call_args
            payload = kwargs["json"]
            self.assertEqual(payload[0], "user")
            self.assertEqual(payload[1], "password")

    def test_login_failed(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '{"success":"false"}'
        mock_response.json.return_value = {"success": "false"}

        with patch.object(self.session, "request", return_value=mock_response):
            self.assertRaises(
                LoginException, self.instance.login, "user", "password", self.session
            )

    def test_login_missing_credentials(self):
        self.assertRaises(LoginException, self.instance.login, session=self.session)

    def test_login_failed_by_status_code(self):
        mock_response = MagicMock()
        mock_response.status_code = 500

        with patch.object(self.session, "request", return_value=mock_response):
            self.assertRaises(
                ResponseException, self.instance.login, "user", "password", self.session
            )

    def test_billed_consumption(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '{"y":{"data":[[{"valor":"1.5"},{"valor":"2.5"}]]}}'
        mock_response.json.return_value = {
            "y": {"data": [[{"valor": "1.5"}, {"valor": "2.5"}]]}
        }

        with patch.object(self.session, "request", return_value=mock_response):
            result = self.instance.billed_consumption(
                date(2024, 1, 1), date(2024, 1, 2)
            )
            self.assertEqual(result, [1.5, 2.5])

    def test_total_billed_consumption(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '{"acumulado":"10.5"}'
        mock_response.json.return_value = {"acumulado": "10.5"}

        with patch.object(self.session, "request", return_value=mock_response):
            result = self.instance.total_billed_consumption(
                date(2024, 1, 1), date(2024, 1, 2)
            )
            self.assertEqual(result, 10.5)


if __name__ == "__main__":
    unittest.main()
