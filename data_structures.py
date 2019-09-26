import errors

class Quote:

    def __init__(self, quantity, price):
        try:
            if isinstance(quantity, int):
                self.quantity = quantity
            else:
                raise errors.NotAnIntegerError

            if isinstance(price, float) or isinstance(price, int):
                self.price = price
            else:
                raise errors.NotANumberError

            self.exchange = ''
            
        except errors.NotAnIntegerError:
            print('Error: The value of the quentity must be an integer')
        except errors.NotANumberError:
            print('Error: The value of the price must be a number')

    def __repr__(self):
        return f'{self.quantity}@{self.price}'
