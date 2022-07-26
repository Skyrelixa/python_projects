class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):        # another way to do it
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooSmallError('Value is too small', x)

try:
    test_value(4)
    
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)