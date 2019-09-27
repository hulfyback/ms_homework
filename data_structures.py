import errors


class Quote:
    
    def __init__(self, quantity, price):
        try:
            if isinstance(quantity, int):
                self.quantity = quantity

                if isinstance(price, float) or isinstance(price, int):
                    self.price = price
                    self.exchange = ''
                else:
                    raise errors.NotAnIntegerError
            else:
                raise errors.NotANumberError
            
        except errors.NotAnIntegerError:
            print('Error: The type of the quantity must be integer')
        except errors.NotANumberError:
            print('Error: The type of the price must be number')

    def __add__(self, other_quote):
        try:
            if isinstance(other_quote, Quote):
                if self.price == other_quote.price:
                    total_qantity = self.quantity + other_quote.quantity
                    price = self.price
                    return Quote(total_qantity, price)
                else:
                    raise ValueError
            else:
                raise TypeError
        except TypeError:
            print('Error: The type of the argument must be Quote')
        except ValueError:
            print('Error: The price of the quotes must be equals')

    def __str__(self):
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

    def __str__(self):
        order_book_str = ''
        i_quotes = iter(self.quotes)
        try:
            order_book_str += f'{next(i_quotes)}'
        except StopIteration:
            return f'{self.name}: {order_book_str}'
        while True:
            try:
                order_book_str += f' | {next(i_quotes)}'
            except StopIteration:
                return f'{self.name}: {order_book_str}'

    def add_quote(self, quote):
        try:
            if isinstance(quote, Quote):
                quote.exchange = self.name
                self.quotes.append(quote)
            else:
                raise TypeError
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

    def __str__(self):
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
