import errors
import collections
import numbers


class Quote:
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

    def __str__(self):
        if self.quotes == []:
            return '()'
        else:
            merged_book_str = ''
            sub_quotes_str = '('
            i_quotes = iter(self.quotes)
            current_quote = next(i_quotes)
            sub_quotes_str += str(current_quote)
            while True:
                try:
                    nxt = next(i_quotes)
                    if nxt.price == current_quote.price:
                        sub_quotes_str += f',{nxt}'
                    else:
                        sub_quotes_str += ')'
                        merged_book_str += f'{sub_quotes_str} | '
                        current_quote = nxt
                        sub_quotes_str = f'({current_quote}'
                except StopIteration:
                    sub_quotes_str += ')'
                    merged_book_str += f'{sub_quotes_str}'
                    break
            return merged_book_str

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
        self.merge_quotes()

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

    @errors.catch_negative_number_error
    @errors.catch_not_a_number_error
    @errors.catch_not_an_int_error
    def simulateBuy(self, quantity, price):
        if isinstance(quantity, int) is False:
            raise errors.NotAnIntegerError
        elif quantity < 0:
            raise errors.NegativeNumberError
        elif isinstance(price, numbers.Number) is False:
            raise errors.NotANumberError
        elif price < 0:
            raise errors.NegativeNumberError
        else:
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

ob1 = OrderBook('LSE')
ob2 = OrderBook('TRQS')
ob3 = OrderBook('BATS')

ob1.add_quote(Quote(100, 0.1))
ob1.add_quote(Quote(200, 0.2))
ob1.add_quote(Quote(300, 0.3))

ob2.add_quote(Quote(100, 0.1))
ob2.add_quote(Quote(200, 0.35))
ob2.add_quote(Quote(300, 0.4))

ob3.add_quote(Quote(100, 0.15))
ob3.add_quote(Quote(400, 0.3))
ob3.add_quote(Quote(200, 0.5))
ob3.add_quote(Quote(300, 0.6))

mb = MergedBook('New Merged Book')

mb.add_orderbook(ob1)
mb.add_orderbook(ob2)
mb.add_orderbook(ob3)

mb.simulateBuy(100, 0.1)
mb.simulateBuy(250, 0.25)
mb.simulateBuy(250, 0.25)
mb.simulateBuy(250, 0.25)

print(mb)
