import unittest


import errors
from quote import Quote

class TestQuote(unittest.TestCase):
    def setUp(self):
        self.quote = Quote(100, 0.1)
        self.other_quote = Quote(50, 0.35)

    def test_adding_quotes(self):
        self.assertEqual(self.quote + self.quote, Quote(200, 0.1))
        self.assertEqual(sum([self.quote, self.quote]), Quote(200, 0.1))

    def test_quote_comparing(self):
        self.assertLess(self.quote, self.other_quote)
        self.assertTrue(self.quote == Quote(300, 0.1))

    def test_quote_to_string(self):
        self.assertEqual(str(self.quote), '100@0.1')
