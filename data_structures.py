import errors
import collections
import numbers


class Quote:
    price= 0
    
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
        elif self.price != other_quote.price or min(self.price, other_quote.price) != 0:
            raise ValueError
        else:
            total_qantity = self.quantity + other_quote.quantity
            return Quote(total_qantity, max(self.price, other_quote.price))

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

class OrderBook:
    
    @errors.catch_type_error(errors.ErrorMessages.STRING)
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
            self.quotes = []
        else: 
            raise TypeError

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

    @errors.catch_type_error(errors.ErrorMessages.QUOTE)
    def add_quote(self, quote):
        if isinstance(quote, Quote):
            quote.exchange = self.name
            self.quotes.append(quote)
        else:
            raise TypeError

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
