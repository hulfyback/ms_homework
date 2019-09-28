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
            print('Error: The type of the quantity must be integer')
        except errors.NotANumberError:
            print('Error: The type of the price must be number')
        except errors.NegativeNumberError:
            print('Error: Input value must be greater then 0')

    def __add__(self, other_quote):
        try:
            if isinstance(other_quote, Quote):
                if self.price == other_quote.price or min(self.price, other_quote.price) == 0:
                    total_qantity = self.quantity + other_quote.quantity
                    return Quote(total_qantity, max(self.price, other_quote.price))
                else:
                    raise ValueError
            else:
                raise TypeError
        except TypeError:
            print('Error: The type of the argument must be Quote')
        except ValueError:
            print('Error: The price of the quotes must be equals')

    def __radd__(self, other_quote):
        if other_quote == 0:
            return self
        else:
            return self.__add__(other_quote)

    def __str__(self):
        return f'{self.quantity}@{self.price}'

    def __eq__(self, other_quote):
        try:
            if isinstance(other_quote, Quote) != True:
                raise TypeError
            else:
                return not self.price < other_quote.price and not other_quote.price < self.price
        except TypeError:
            print('Error: The type of the argument must be Quote')

    def __ge__(self, other_quote):
        try:
            if isinstance(other_quote, Quote) != True:
                raise TypeError
            else:
                return not self.price < other_quote.price
        except TypeError:
            print('Error: The type of the argument must be Quote')

    def __le__(self, other_quote):
        try:
            if isinstance(other_quote, Quote) != True:
                raise TypeError
            else:
                return not other_quote.price < self.price
        except TypeError:
            print('Error: The type of the argument must be Quote')

    def __gt__(self, other_quote):
        try:
            if isinstance(other_quote, Quote) != True:
                raise TypeError
            else:
                return other_quote.price < self.price
        except TypeError:
            print('Error: The type of the argument must be Quote')

    def __lt__(self, other_quote):
        try:
            if isinstance(other_quote, Quote) != True:
                raise TypeError
            else:
                return self.price < other_quote.price
        except TypeError:
            print('Error: The type of the argument must be Quote')
