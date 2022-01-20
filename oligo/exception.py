class IberException(Exception):
    pass


class ResponseException(IberException):
    pass


class LoginException(IberException):
    pass


class SessionException(IberException):
    pass


class NoResponseException(IberException):
    pass


class SelectContractException(IberException):
    pass
