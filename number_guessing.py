import random

high=10
low=1
answer=random.randint(low,high)

print('Please guess a number between {} and {}.'.format(low,high))
your_answer=int(input())
while True:
    print('guessing in the range of {} and {}.'.format(low,high))
    if your_answer>answer:
        print('you need to go lower')
    elif your_answer<answer:
        print('you need to go higher')
    else:
        print('you got it!')
        break
    your_answer=int(input())

