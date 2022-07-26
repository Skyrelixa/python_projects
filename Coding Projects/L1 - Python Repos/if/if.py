is_male = False
is_tall = True

# can replace and with &, but then cannot put "and not"
if not is_male and is_tall:
    print("It is NOT a male and it is tall.\n")

is_male = False
is_tall = False

# can replace or with |, but then cannot put "or not"
if is_male or is_tall:
    print("It is a male OR is tall.\n")

elif not is_male and not is_tall:
    print("NOT a male AND NOT tall")

else:
    print("It is NOT a male or it is NOT tall.")