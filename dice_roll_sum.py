import random

high = 6
low = 1
guesses = 1

print('Roll two dices. What should your two dice rolls equal to? ')
my_guess = int(input())
first_roll = random.randint(low, high)
second_roll = random.randint(low, high)
rolls_sum = first_roll + second_roll

while True:
    print(input('Press ENTER to roll the dice: '))
    first_roll = random.randint(low, high)
    print(first_roll)
    print(input('Press ENTER to roll again: '))
    second_roll = random.randint(low, high)
    print(second_roll)
    rolls_sum = first_roll + second_roll
    print('Your two rolls equals to {}. '.format(rolls_sum))
    if rolls_sum < my_guess:
        print('You guessed too high! Guess and roll again.')
        my_guess = int(input('My new guess is: '))
    elif rolls_sum > my_guess:
        print('You guessed too low! Guess and roll again.')
        my_guess = int(input('My new guess is: '))
    else:
        print('You got it in {} guesses!'.format(guesses))
        break
    guesses = guesses + 1
