from enum import Enum


class ErrorMessages(Enum):
    def __str__(self):
        return str(self.value)
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

def catch_type_error(postfix):
    def outer_wrapper_func(func):
        def wrapper_func(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except TypeError:
                print(ErrorMessages.QUOTE)
        return wrapper_func
    return outer_wrapper_func

def catch_value_error(func):
    def wrapper_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print('Error: The price of the quotes must be equals')
    return wrapper_func

def catch_not_an_int_error(func):
    def wrapper_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotAnIntegerError:
            print(NotAnIntegerError.error_msg)
    return wrapper_func

def catch_not_a_number_error(func):
    def wrapper_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotANumberError:
            print(NotANumberError.error_msg)
    return wrapper_func

def catch_negative_number_error(func):
    def wrapper_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NegativeNumberError:
            print(NegativeNumberError.error_msg)
    return wrapper_func
