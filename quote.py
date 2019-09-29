import errors
import numbers


class Quote:
    quantity = None
    price = None
    
    @errors.catch_not_an_int_error
    @errors.catch_not_a_number_error
    @errors.catch_negative_number_error
    def __init__(self, quantity=0, price=0):
        if isinstance(quantity, int) is False:
            raise errors.NotAnIntegerError
        elif isinstance(price, numbers.Number)is False:
            raise errors.NotANumberError
        elif quantity < 0 or price < 0:
            raise errors.NegativeNumberError
        else:
            self.quantity = quantity        
            self.price = price
            self.exchange = ''

    @errors.catch_type_error(errors.ErrorMessages.QUOTE)
    @errors.catch_value_error
    def __add__(self, other_quote):
        if isinstance(other_quote, Quote) is False:
            raise TypeError
        elif self.price == other_quote.price or min(self.price, other_quote.price) == 0:            
            total_qantity = self.quantity + other_quote.quantity
            return Quote(total_qantity, max(self.price, other_quote.price))
        else:
            raise ValueError
    
    @errors.catch_type_error(errors.ErrorMessages.QUOTE)
    def __radd__(self, other_quote):
        if other_quote == 0:
            return self
        elif isinstance(other_quote, Quote) is False:
            raise TypeError
        else:
            return self.__add__(other_quote)

    def __str__(self):
        return f'{self.quantity}@{self.price}'

    @errors.catch_type_error(errors.ErrorMessages.QUOTE)
    def __eq__(self, other_quote):
        if isinstance(other_quote, Quote) != True:
            raise TypeError
        else:
            return not self.price < other_quote.price and not other_quote.price < self.price

    @errors.catch_type_error(errors.ErrorMessages.QUOTE)
    def __ge__(self, other_quote):
        if isinstance(other_quote, Quote) != True:
            raise TypeError
        else:
            return not self.price < other_quote.price

    @errors.catch_type_error(errors.ErrorMessages.QUOTE)
    def __le__(self, other_quote):
        if isinstance(other_quote, Quote) != True:
            raise TypeError
        else:
            return not other_quote.price < self.price

    @errors.catch_type_error(errors.ErrorMessages.QUOTE)
    def __gt__(self, other_quote):
        if isinstance(other_quote, Quote) != True:
            raise TypeError
        else:
            return other_quote.price < self.price

    @errors.catch_type_error(errors.ErrorMessages.QUOTE)
    def __lt__(self, other_quote):
        if isinstance(other_quote, Quote) != True:
            raise TypeError
        else:
            return self.price < other_quote.price
