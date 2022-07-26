from itertools import accumulate

a = [1,2,3,4]
acc = accumulate(a)

print(list(acc))

import operator

acc = accumulate(a, func=operator.mul)      # other function includes max
print(a)
print(list(acc))