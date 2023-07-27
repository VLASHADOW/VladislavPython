from random import randint


def is_valid(number):
    return number > 100 or number < 1


n = randint(1, 100)
print('Welcome to number guessing')
num = int(input('Enter the number: '))
s = 'Yes'
if is_valid(num):
    print('The number isn`t in range, try again)')
else:
    while s == 'Yes':
        counter = 0
        while n != num:
            if num < n:
                print('Your number is less than expected, try again')
                num = int(input('Enter the number: '))
            else:
                print('Your number is more than expected, try again')
                num = int(input('Enter the number: '))
            counter += 1
        print('Hooray, hooray, hooray!!! You guessed it, congratulations!')
        print("It took you ", counter, " tries")
        s = input('Do you want to play again? ')
        if s == "Yes":
            num = int(input('Enter the number: '))
            n = randint(1, 100)
        else:
            break
print('Thanks for playing the number guessing game. See you...')
