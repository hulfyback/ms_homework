import unittest

import errors
from quote import Quote
from order_book import OrderBook


class TestOrderBook(unittest.TestCase):
    def setUp(self):
        self.quote = Quote(100, 0.1)
        self.order_book = OrderBook('LSE')

    def test_order_book_into_string(self):
        self.order_book.add_quote(self.quote)
        self.assertEqual(str(self.order_book), 'LSE: 100@0.1')
        self.order_book.add_quote(self.quote)
        self.assertEqual(str(self.order_book), 'LSE: 100@0.1 | 100@0.1')

    def test_add_quote(self):
        self.order_book.add_quote(self.quote)      
        self.assertEqual(self.order_book.quotes, [self.quote])
        self.assertEqual(self.order_book.name, self.order_book.quotes[0].exchange)

if __name__ == '__main__':
    unittest.main()   
