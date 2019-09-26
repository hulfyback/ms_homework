import errors

class Quote:

    def __init__(self, quantity, price):
        try:
            self.quantity = quantity
            if quantity.__class__() != 0:
                raise errors.NotAnIntegerError

            self.price = price
            if price.__class__() != 0 or price.__class__() != 0.0:
                raise errors.NotANumberError
            
        except errors.NotAnIntegerError:
            print('Error: The value of the quentity must be an integer')
        except errors.NotANumberError:
            print('Error: The value of the price must be a number')

    def __repr__(self):
        return f'{self.quantity}@{self.price}'
