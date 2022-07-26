# STRINGS
char_name = "Pyra"
char_num = "35"

#.upper() UPPERCASE .lower() lowercase
print("\n" + char_name.upper() + " wants to eat " + char_num + " cookies.")

# data overwritten
char_name = "New"
char_num = "45"

#.isupper() checks for UPPERCASE. can concatenate functions
print("\n" + char_name.upper() + " wants to eat " + char_num + " cookies.\n")
print(char_name.upper().isupper())
# expect output True

# len(x) can check length of phrase
print(len(char_name))
# expect output 3

# treating char like an array to obtain first char
print(char_name[0])
# expect output N

# finding letters in string, outputs starting location
print(char_name.index("Ne"))
# expect output 0. can also use find()

# replace function, 2 params. replacing string
print(char_name.replace("New","Old"))

# BOOLEANS
is_male = False
is_female = True