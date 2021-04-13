hangman_answer = 'S, p, o, n, g, e, b, o, b'.casefold()
hangman_list = []
guesses = 5
user_guess = input("What is your first letter guess? ").casefold()


def spongebob_list(string):
    list_answer = list(hangman_answer.split(" "))
    return list_answer

s_list = 'Spongebob'
print(spongebob_list(s_list))
# How to convert string to list?

while user_guess != hangman_answer:
    if user_guess in hangman_answer:
        # What function can have the letter that user guessed be shown
        # each time after another like in Hangman?
        hangman_list.append(user_guess)
        print(hangman_list)
        print('Good job!')
        user_guess = input("What is your next letter guess? ")
    if hangman_list == spongebob_list(s_list):
        print('Well done!')
    elif user_guess not in hangman_answer:
        print('Wrong guess. You have {} guesses remaining.'.format(guesses))
        user_guess = input("Guess again. ")
        guesses -= 1
        if guesses == 0:
            print('Game Over')
            break
