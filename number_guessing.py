import random

high = 10
low = 1
guesses = 3
answer = random.randint(low, high)

print('Please guess a number between {} and {}.'.format(low, high))
your_answer = int(input())
while True:
    if guesses == 0:
        print('You took too many guesses. Play again.')
        break
    elif your_answer > answer:
        print('You need to go lower.')
        print('You have {} guesses remaining.'.format(guesses))
    elif your_answer < answer:
        print('You need to go higher.')
        print('You have {} guesses remaining.'.format(guesses))
    else:
        print('Good guess. You got it!')
        break
    your_answer = int(input())
    guesses -= 1
