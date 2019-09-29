import unittest

import errors
from quote import Quote
from order_book import OrderBook
from merged_book import MergedBook


class TestMergedBook(unittest.TestCase):
    def setUp(self):
        self.order_book_lse = OrderBook('LSE')
        self.order_book_lse.add_quotes([Quote(100, 0.1), Quote(200, 0.2), Quote(300, 0.3)])
        self.order_book_trqs = OrderBook('TRQS')
        self.order_book_trqs.add_quotes([Quote(100, 0.1), Quote(200, 0.35), Quote(300, 0.4)])
        self.order_book_bats = OrderBook('BATS')
        self.order_book_bats.add_quotes([Quote(100, 0.15), Quote(400, 0.3), Quote(200, 0.5), Quote(300, 0.6)])
        self.merged_book = MergedBook('MB')

    def test_add_order_book(self):
        self.merged_book.add_orderbook(self.order_book_lse)
        self.assertEqual(self.merged_book.quotes, self.order_book_lse.quotes)
        self.merged_book.add_orderbook(self.order_book_bats)
        self.assertEqual(self.merged_book.quotes, self.order_book_lse.quotes + [self.order_book_bats.quotes[1],
                self.order_book_bats.quotes[0], self.order_book_bats.quotes[2], self.order_book_bats.quotes[3]])

    def test_merged_book_to_string(self):
        self.merged_book.add_orderbook(self.order_book_lse)
        self.assertEqual(str(self.merged_book), '(100@0.1) | (200@0.2) | (300@0.3)')

    def test_merging_order_books(self):
        self.merged_book.add_orderbook(self.order_book_lse)
        self.merged_book.add_orderbook(self.order_book_trqs)
        self.assertTrue(len(self.merged_book.quotes) == 6)
        self.merged_book.merge_quotes()
        self.assertTrue(len(self.merged_book.quotes) == 5)
        self.merged_book.add_orderbook(self.order_book_bats)
        self.assertTrue(len(self.merged_book.quotes) == 9)
        self.merged_book.merge_quotes()
        self.assertTrue(len(self.merged_book.quotes) == 8)
        self.assertEqual(self.merged_book.quotes[0], Quote(200, 0.1))

    def test_simulateBuy(self):
        self.merged_book.add_orderbook(self.order_book_lse)
        self.merged_book.add_orderbook(self.order_book_trqs)
        self.merged_book.add_orderbook(self.order_book_bats)
        self.merged_book.simulateBuy(100, 0.1)
        self.merged_book.simulateBuy(250, 0.25)
        self.assertEqual(self.merged_book.quotes, [Quote(150, 0.2), Quote(700, 0.3), Quote(200, 0.35), 
        Quote(300, 0.4), Quote(200, 0.5), Quote(300, 0.6)])

if __name__ == '__main__':
    unittest.main()   
