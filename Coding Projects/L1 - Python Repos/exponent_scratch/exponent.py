def exponent(base_num, power):
    result = 1
    for i in range(power):
        result = result * base_num
    return result

print(exponent(3,4))