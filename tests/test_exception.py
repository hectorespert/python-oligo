import unittest

from oligo.exception import SessionException, LoginException, ResponseException


class TestResponseException(unittest.TestCase):

    def test_message(self):
        login_exception = ResponseException(418)
        self.assertEqual('Response error, code: 418', login_exception.args[0])


class TestLoginException(unittest.TestCase):

    def test_message(self):
        login_exception = LoginException("pepe")
        self.assertEqual('Unable to log in with user pepe', login_exception.args[0])


class TestSessionException(unittest.TestCase):

    def test_message(self):
        session_exception = SessionException()
        self.assertEqual('Session required, use login() method to obtain a session', session_exception.args[0])
