class HRSystemError(Exception):
    """Base Exception for the HR system application"""
    pass


class ValidationError(HRSystemError):
    pass


class UserAlreadyExistError(HRSystemError):
    pass


class AuthenticationError(HRSystemError):
    pass


class NotFoundError(HRSystemError):
    pass


class AuthorizationError(HRSystemError):
    pass