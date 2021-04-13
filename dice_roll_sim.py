import random

high = 6
low = 1
guesses = 1

print('What should your two dice rolls equal to? ')
myguess = int(input())
print(input('Press ENTER to roll the dice: '))
roll = random.randint(low, high)
print(roll)
print(input('Press ENTER to roll again. '))
roll2 = random.randint(low, high)
print(roll2)
rolls_total = roll + roll2
print('Your two rolls equals to {}. '.format(rolls_total))
#added a comment in intellij
while True:
    if rolls_total == myguess:
        print('You got it in {} guesses!'.format(guesses))
        break
    elif myguess>rolls_total:
        print('You need to guess lower! Roll again.')
        print(input('Press ENTER to roll again. '))
        roll = random.randint(low, high)
        print(roll)
        print(input('Press ENTER to roll again. '))
        roll2 = random.randint(low, high)
        print(roll2)
        rolls_total = roll + roll2
        print('Your rolls are equal to {}'.format(rolls_total))
    elif myguess<rolls_total:
        print('You need to guess higher! Roll again.')
        print(input('Press ENTER to roll again.'))
        roll = random.randint(low, high)
        print(roll)
        print(input('Press ENTER to roll again.'))
        roll2 = random.randint(low, high)
        print(roll2)
        rolls_total = roll + roll2
        print('Your rolls are equal to {}'.format(rolls_total))
        #line won't rund past a certain amount
    guesses = guesses + 1
