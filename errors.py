class Error(Exception):
    pass

class NotAnIntegerError(Error):
    """Raised when the input value is not an integer"""
    pass

class NotANumberError(Error):
    """Raised when the input value is not a number"""
    pass

class NegativeNumberError(Error):
    """Raised when the input value is lower then zero"""
    pass
