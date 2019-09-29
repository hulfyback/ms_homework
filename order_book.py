import errors
from quote import Quote


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
    @errors.catch_type_error(errors.ErrorMessages.LIST)
    def add_quotes(self, quotes):
        if isinstance(quotes, list) is False:
            raise TypeError
        else:
            for quote in quotes:
                self.add_quote(quote)
