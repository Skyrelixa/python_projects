from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)      # can also use lambda funct, key=lambda x: x<3

# print(list(group_obj))      # not optimal

# for key, val in group_obj:      # not optimal
#     print(key, val)

for key, val in group_obj:
    print(key, list(val))

persons = [
    dict(name='Tim', age=25),
    dict(name='Dan', age=25),
    dict(name='Lisa', age=27),
    dict(name='Claire', age=28)
]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, val in group_obj:
    print(key, list(val))