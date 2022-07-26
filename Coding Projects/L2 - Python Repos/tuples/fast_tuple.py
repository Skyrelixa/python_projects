# tuples can be more efficient than lists when working with large data
# tuples make programs more compact

import sys

my_list = [0, 1, 2, "hello", True]
my_tuple = 0, 1, 2, "hello", True

print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# tuples make programs FASTER

import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number = 1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number = 1000000))