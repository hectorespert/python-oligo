class IberException(Exception):
    pass


class ResponseException(IberException):
    def __init__(self, status_code):
        super().__init__("Response error, code: {}".format(status_code))


class LoginException(IberException):
    def __init__(self):
        super().__init__('Login error, bad login')


class SessionException(IberException):
    def __init__(self):
        super().__init__('Session required, use login() method to obtain a session')


class NoResponseException(IberException):
    pass


class SelectContractException(IberException):
    pass
