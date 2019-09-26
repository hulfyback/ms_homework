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
                quote.exchange = self.name
                self.quotes.append(quote)
        except TypeError:
            print('Error: Type of the argument must be Quote')

class MergedBook:
    def __init__(self, name):
        self.name = name
        self.quotes = []

    def add_orderbook(self, orderbook):
        for quote in orderbook.quotes:
            if self.quotes == []:
                self.quotes.append(quote)
            else:
                i_quotes = iter(self.quotes)
                indexes = iter(range(len(self.quotes) - 1))
                while True:
                    try:
                        next_index = next(indexes)
                        nxt = next(i_quotes)
                        if nxt.price == quote.price:
                            self.quotes.insert(next_index + 1, quote)
                            break
                    except StopIteration:
                        self.quotes.append(quote)
                        break


    def __repr__(self):
        if self.quotes == []:
            return '()'
        else:
            merged_book_repr = ''
            sub_quotes_repr = '('
            i_quotes = iter(self.quotes)
            current_quote = next(i_quotes)
            sub_quotes_repr += repr(current_quote)
            while True:
                try:
                    nxt = next(i_quotes)
                    if nxt.price == current_quote.price:
                        sub_quotes_repr += f',{nxt}'
                    else:
                        sub_quotes_repr += ')'
                        merged_book_repr += f'{sub_quotes_repr} | '
                        current_quote = nxt
                        sub_quotes_repr = f'({current_quote}'
                except StopIteration:
                    sub_quotes_repr += ')'
                    merged_book_repr += f'{sub_quotes_repr}'
                    break
            return merged_book_repr
