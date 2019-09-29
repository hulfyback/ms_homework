import collections
import numbers

import errors
from quote import Quote
from order_book import OrderBook


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
