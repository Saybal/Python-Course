monthCOnversion = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'Octobober',
    11: 'November',
    12: 'December'
}

monthCOnversion[13] = 'random' #insert value from putside

month_num = int(input('Enter a month number: '))
# print('Your month is: ', monthCOnversion[month_num])
print('Your month is: ', monthCOnversion.get(month_num))