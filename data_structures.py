import errors


class Quote:

    def __init__(self, quantity, price):
        try:
            if isinstance(quantity, int):
                if quantity > 0:
                    self.quantity = quantity
                else:
                    raise errors.NegativeNumberError
    
                if isinstance(price, float) or isinstance(price, int):
                    if price > 0:
                        self.price = price
                        self.exchange = ''
                    else:
                        raise errors.NegativeNumberError
                else:
                    raise errors.NotAnIntegerError
            else:
                raise errors.NotANumberError
            
        except errors.NotAnIntegerError:
            print('Error: The type of the quentity must be integer')
        except errors.NotANumberError:
            print('Error: The type of the price must be number')
        except errors.NegativeNumberError:
            print('Error: Input value must be greater then 0')

    def __add__(self, other_quote):
        try:
            if isinstance(other_quote, Quote):
                if self.price == other_quote.price:
                    total_qantity = self.quantity + other_quote.quantity
                    price = self.price
                    return Quote(total_qantity, price)
                else:
                    raise ValueError
            else:
                raise TypeError
        except TypeError:
            print('Error: The type of the argument must be Quote')
        except ValueError:
            print('Error: The price of the quotes must be equals')

    def __str__(self):
        return f'{self.quantity}@{self.price}'
