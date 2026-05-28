# for letter in 'Saybal Roy':
#     print(letter)

# odd = [1,3,5,7,9]
# for num in odd:
#     print(num)

# for i in range(10):
#     print(i)

# for i in range(4,10):
#     print(i)

# for i in range(len(odd)):
#     print(odd[i])

#!exponent
print(2**3)
print(pow(2,3))

def exponent(base, power):
    result = 1
    for i in range(power):
        result *= base
    return result

print(exponent(2,3))