import errors
import collections


class Quote:
    
    def __init__(self, quantity=0, price=0):
        try:
            if isinstance(quantity, int):
                if quantity >= 0:
                    self.quantity = quantity
                else:
                    raise errors.NegativeNumberError
    
                if isinstance(price, float) or isinstance(price, int):
                    if price >= 0:
                        self.price = price
                        self.exchange = ''
                    else:
                        raise errors.NegativeNumberError
                else:
                    raise errors.NotAnIntegerError
            else:
                raise errors.NotANumberError
            
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
                if quote.exchange == '':
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
            sub_quotes_repr += str(current_quote)
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

    def merge_quotes(self):
        merged_quotes = collections.defaultdict(Quote)
        for quote in self.quotes:
            merged_quotes[quote.price] += quote
                
        new_order_book = OrderBook(self.name)
        for quote in merged_quotes.values():
            new_order_book.add_quote(quote)
        new_merged_book = MergedBook(self.name)
        new_merged_book.add_orderbook(new_order_book)
        return new_merged_book

    def simulateBuy(self, quantity, price):
        pass
    