# Define a new function to check if user entered a string.
print(input('Press ENTER to begin: '))
print('What is your name?')
user_answer = input().capitalize()
print('Welcome {}. Are you ready to begin your adventure?'.format(user_answer))
game_over = 'exit'
user_answer = input('Yes or no? ')
print('Welcome brave one. Enter EXIT at any time to quit game.')
print()

while 'exit' not in user_answer:
    if 'yes' in user_answer:
        print("You reach a fork in the road and see two paths. One leads to a "
        "forest and the other to the beach. Which path do you choose?")
        user_answer = input('Forest or beach? ').casefold()
        if 'forest' in user_answer:
            print('You walk along the forest but a bear sees you.')
            user_answer = input('Do you run? Yes or no? ')
            if 'yes' in user_answer:
                print('')
            elif 'no' in user_answer:
                print('')

        elif 'beach' in user_answer:
            print("You walk along the beach and see a fin poking out of the "
            "water.")
            user_answer = input('Do you investigate? Yes or no? ')
            if 'yes' in user_answer:
                print('')
            elif 'no' in user_answer:
                print('')

    elif 'no' in user_answer:
        print('You need courage in your life. Until next time.')
        break
else:
    print('Game Over')
