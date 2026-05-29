try:
    # value = 100/0
    num = int(input("Enter a number: "))
    print(num)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)