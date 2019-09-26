class Error(Exception):
    pass

class NotAnIntegerError(Error):
    """Raised when the input value is not an integer"""
    pass

class NotANumberError(Error):
    """Raised when the input value is not a number"""
    pass
