import errors


class Quote:
    price= None
    
    def __init__(self, quantity=0, price=0):
        try:
            if isinstance(quantity, int) is False:
                raise errors.NotAnIntegerError
            elif isinstance(price, float) is False or isinstance(price, int) is False:
                raise errors.NotANumberError
            elif quantity < 0 or price < 0:
                raise errors.NegativeNumberError
            else:
                self.quantity = quantity        
                self.price = price
                self.exchange = ''            
        except errors.NotAnIntegerError:
            print(errors.NotANumberError.error_msg)
        except errors.NotANumberError:
            print(errors.NotANumberError.error_msg)
        except errors.NegativeNumberError:
            print(errors.NegativeNumberError.error_msg)

    def __add__(self, other_quote):
        try:
            if isinstance(other_quote, Quote) is False:
                raise TypeError
            elif self.price != other_quote.price or min(self.price, other_quote.price) != 0:
                raise ValueError
            else:
                total_qantity = self.quantity + other_quote.quantity
                return Quote(total_qantity, max(self.price, other_quote.price))
        except TypeError:
            print(errors.ErrorMessages.QUOTE)
        except ValueError:
            print('Error: The price of the quotes must be equals')

    def __radd__(self, other_quote):
        try:
            if other_quote == 0:
                return self
            elif isinstance(other_quote, Quote) is False:
                raise TypeError
            else:
                return self.__add__(other_quote)
        except TypeError:
            print(errors.ErrorMessages.QUOTE)

    def __str__(self):
        return f'{self.quantity}@{self.price}'

    def __eq__(self, other_quote):
        try:
            if isinstance(other_quote, Quote) != True:
                raise TypeError
            else:
                return not self.price < other_quote.price and not other_quote.price < self.price
        except TypeError:
            print(errors.ErrorMessages.QUOTE)

    def __ge__(self, other_quote):
        try:
            if isinstance(other_quote, Quote) != True:
                raise TypeError
            else:
                return not self.price < other_quote.price
        except TypeError:
            print(errors.ErrorMessages.QUOTE)

    def __le__(self, other_quote):
        try:
            if isinstance(other_quote, Quote) != True:
                raise TypeError
            else:
                return not other_quote.price < self.price
        except TypeError:
            print(errors.ErrorMessages.QUOTE)

    def __gt__(self, other_quote):
        try:
            if isinstance(other_quote, Quote) != True:
                raise TypeError
            else:
                return other_quote.price < self.price
        except TypeError:
            print(errors.ErrorMessages.QUOTE)

    def __lt__(self, other_quote):
        try:
            if isinstance(other_quote, Quote) != True:
                raise TypeError
            else:
                return self.price < other_quote.price
        except TypeError:
            print(errors.ErrorMessages.QUOTE)
