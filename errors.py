from enum import Enum


class ErrorMessages(Enum):
    msg = 'Error: The type of the argument must be '
    QUOTE = f'{msg} Quote'

class Error(Exception):
    pass

class NotAnIntegerError(Error):
    """Raised when the input value is not an integer"""
    error_msg = 'Error: The Type of the argument must be integer'
    pass

class NotANumberError(Error):
    """Raised when the input value is not a number"""
    error_msg = 'Error: The Type of the argument must be number'
    pass

class NegativeNumberError(Error):
    """Raised when the input value is lower then zero"""
    error_msg = 'Error: The value of the argument must be greater then 0'
    pass
