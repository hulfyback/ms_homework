import errors

class Quote:

    def __init__(self, quantity, price):
        try:
            if quantity.__class__() != 0:
                raise errors.NotAnIntegerError
            else:
                self.quantity = quantity

            if price.__class__() != 0 or price.__class__() != 0.0:
                raise errors.NotANumberError
            else:
                self.price = price
            
        except errors.NotAnIntegerError:
            print('Error: The type of the quentity must be an integer')
        except errors.NotANumberError:
            print('Error: The type of the price must be a number')

    def __repr__(self):
        return f'{self.quantity}@{self.price}'

class OrderBook:

    def __init__(self, name):
        try:
            if name.__class__() != '':
                raise TypeError
            else: 
                self.name = name
                self.quotes = []
        except TypeError:
            print('Error: The type of the name must be a string')

    def __repr__(self):
        order_book_repr = ''
        for quote in self.quotes:
            order_book_repr += f'{quote.__repr__()} | '
        return order_book_repr

    def add_quote(self, quote):
        try:
            if len(str(quote.__class__).split('.')) == 1 or str(quote.__class__).split('.')[1].split("'")[0] != 'Quote':
                raise TypeError
            else:
                self.quotes.append(quote)
        except TypeError:
            print('Error: Type of the argument must be Quote')

class MergedBook:
    def __init__(self, name):
        self.name = name
        self.quotes = []

    def add_orderbook(self, orderbook):
        for quote in orderbook:
            for i in len(self.quotes - 1):
                if quote.price == self.quotes[i].price:
                    self.quotes.insert(i, quote)
                    break
                if i == len(self.quotes - 1):
                    self.quotes.append(quote)
