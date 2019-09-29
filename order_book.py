import errors
from quote import Quote


class OrderBook:
    '''
    Datastructure to represent an order book.

    Attributes:
        name (str): Name of the order book.
    '''
    
    @errors.catch_type_error(errors.ErrorMessages.STRING)
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
            self.quotes = []
        else: 
            raise TypeError

    def __str__(self):
        '''
        Represents the order book in a string.

        Args:
            None.
        
        Returns:
            A string e.g.: 100@0.1 | 200@0.25
        '''
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
        '''
        Add a quote to the order book.

        Args:
            quote: Quote to be added to the order book.

        Returns:
            None. The quote will be added to the original order book.

        Raises:
            TypeError: An error occured if the argument is not a Quote.
        '''
        if isinstance(quote, Quote):
            quote.exchange = self.name
            self.quotes.append(quote)
        else:
            raise TypeError

    @errors.catch_type_error(errors.ErrorMessages.LIST)
    def add_quotes(self, quotes):
        '''
        Add a list of quotes to the order book.

        Args:
            quotes (list): List of quotes to be added.

        Returns:
            None. The quotes will be added to the original order book.

        Raises:
            TypeError: An error occured if the argument is not a list of Quotes"
        '''
        if isinstance(quotes, list) is False:
            raise TypeError
        else:
            for quote in quotes:
                self.add_quote(quote)
