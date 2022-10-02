

secret_word = 'lion'
guess = ""
guess_count = 0
max_limit = 3
out_of_guess = False

while guess != secret_word and not(out_of_guess):
    if guess_count < max_limit:
        guess = input('Enter the guess Word : ')
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess == True:
    print('you loose')
else:
    print('you won')