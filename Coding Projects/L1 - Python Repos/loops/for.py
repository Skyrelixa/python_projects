# prints the letters
for letter in "Giraffe Academy":
    print(letter)

# prints the list of friends
friends = ["Jim", "Karen", "Kimmy"]

for friend in friends:
    print(friend)

# prints every number from 3 to 9
for index in range(3, 10):
    print(index)

# prints the friends in the array for the range of the array
for index in range(len(friends)):
    print(friends[index])

# what if we want to do something different on the first iteration?
for index in range(5):
    if index == 0:
        print("First iteration")
    else:
        print(" Not first")
