def max_num(num1, num2, num3):
    if num1 >= num2 and num1>= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 20, 1))

def strings(str1, str2):
    if str1 != str2:
        print("The strings do not match.")
    else:
        print("The strings match.")

strings("Dog", "Cat")