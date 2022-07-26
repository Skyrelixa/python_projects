lucky_numbers = [4,8,15,16,23,42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# print(friends)

# EXTEND
friends.extend(lucky_numbers)
print(friends)

# APPEND
friends.append("Creed")
print(friends)

# INSERT
friends.insert(3, "Nooooooob")
print(friends)

# REMOVE
friends.remove("Jim")
print(friends)

# CLEAR
friends.clear()
print(friends)

# POP
friends.append("Jim")
friends.pop()
print(friends)

# COUNT
friends.append("Jim")
print(friends.count("Jim"))

# SORT
friends.insert(1, "Kate")
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

# REVERSE
lucky_numbers.reverse()
print(lucky_numbers)

# COPY
friends2 = friends.copy()
print(friends2)