def operation(num1,num2, opr):
    if opr == '+':
        return num1 + num2
    elif opr == '-':
        return num1 - num2
    elif opr == '*':
        return num1 * num2
    elif opr == '/':
        return num1 / num2
    else:
        return 0

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))
opr = input('Enter an oprator(+, - , * , /): ')

result = operation(num1, num2, opr)

if(result != 0):
    print('Result: ', result)
else:
    print('Please select a valid operator')

