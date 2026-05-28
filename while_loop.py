# i = 1
# while i <= 10:
#     print(i)
#     i += 1

secret_word = 'Glib'
guess = input('Input our secret word: ')
i = 1

while i<=10 and guess != secret_word:
    print('Wrong!!')
    print('You left ' + str(10-i) + ' chances..')
    guess = input('Guess again: ')
    i += 1

if(i<=10):
    print('You win!!')
else:
    print('You lose!!')