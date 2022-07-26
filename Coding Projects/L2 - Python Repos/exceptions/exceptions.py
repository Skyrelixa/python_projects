x = -5
# if x < 0:
#     raise Exception('x should be positive')

#assert (x>=0), 'x is not positive'

# can also use a try, except block
try:
    a = 5/1
    b = a + '10'
except ZeroDivisionError:
    print('division by zero')
except TypeError as e:
    print(e)
else:                       # runs if no exception occurs
    print('tests went well')
finally:                    # runs regardless of exceptions, used for cleanup operations
    print('cleaning up')

# try:                      not good practice, should specify the type of error as above
#     a = 5/0
# except Exception as e:
#     print(e)