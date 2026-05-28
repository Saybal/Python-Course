# num1 = int(input("Enter a number: "))

# if (num1 % 2 == 1 and num1 > 9):
#     print(str(num1) + ' is an odd number')
# elif (num1 % 2 == 1 and num1 < 9):
#     print(str(num1) + ' is an odd digit')
# elif (num1 % 2 == 0 and num1 < 9):
#     print(str(num1) + ' is an even digit')
# else:
#     print(str(num1) + ' is an even number')

def max_num (num1, num2, num3):
    if(num1 >= num2 and num1 >= num3):
        return num1
    elif(num2 >= num1 and num2 >= num3):
        return num2
    else:
        return num3
    
maximum = max_num(2,5,1)
print(maximum)
