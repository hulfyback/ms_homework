import errors
import collections


class Quote:
    price= None
    
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
        new_order_book.quotes.sort(key=Quote.price)
        self.quotes = []
        self.add_orderbook(new_order_book)
        del(new_order_book)
        return self

    def simulateBuy(self, quantity, price):
        try:
            if isinstance(quantity, int) != True:
                raise errors.NotAnIntegerError
            elif quantity < 0:
                raise errors.NegativeNumberError
            elif isinstance(price, int) or isinstance(price, float) != True:
                raise errors.NotANumberError
            elif price < 0:
                raise errors.NegativeNumberError
            else:
                self.merge_quotes()
                while len(self.quotes) > 0:
                    current_quote = self.quotes[0]
                    if current_quote.price > price:
                        return self
                    elif current_quote.quantity > quantity:
                        current_quote.quantity -= quantity
                        return self
                    else:
                        price -= current_quote.price
                        quantity -= current_quote.quantity
                        self.quotes.remove(current_quote)
        except errors.NotAnIntegerError:
            print('Error: Type of the argument `quantity` must be integer')
        except errors.NotANumberError:
            print('Error: Type of the argument `price` must be number')
        except errors.NegativeNumberError:
            print('Error: Value of the arguments must be greater then 0')
