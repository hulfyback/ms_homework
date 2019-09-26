import errors

class Quote:

    def __init__(self, quantity, price):
        try:
            if isinstance(quantity, int):
                self.quantity = quantity
            else:
                raise errors.NotAnIntegerError

            if isinstance(price, float) or isinstance(price, int):
                self.price = price
            else:
                raise errors.NotANumberError

            self.exchange = ''
            
        except errors.NotAnIntegerError:
            print('Error: The type of the quentity must be an integer')
        except errors.NotANumberError:
            print('Error: The type of the price must be a number')

    def __repr__(self):
        return f'{self.quantity}@{self.price}'

class OrderBook:

    def __init__(self, name):
        try:
            if isinstance(name, str):
                self.name = name
                self.quotes = []
            else: 
                raise TypeError
        except TypeError:
            print('Error: The type of the name must be a string')

    def __repr__(self):
        order_book_repr = ''
        for quote in self.quotes:
            order_book_repr += f'{quote} | '
        return order_book_repr

    def add_quote(self, quote):
        try:
            if isinstance(quote, Quote):
                quote.exchange = self.name
                self.quotes.append(quote)
            else:
                raise TypeError
        except TypeError:
            print('Error: Type of the argument must be Quote')
