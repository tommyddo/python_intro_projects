word_to_guess = 'Spongebob'.casefold()  # Word can be changed.
words_in_list = []
guesses = 5  # Amount of guesses can be changed.
user_guess = input("What is your first letter guess? ").casefold()

while user_guess != word_to_guess:
    # What statement can be used to end game after the entire word is guessed
    # correctly?
    if user_guess in word_to_guess:
        words_in_list.append(user_guess)
        print(words_in_list)
        # How do we remove the commas after each appended letter in list so
        # that it looks like the original word?
        user_guess = input("Good job! What is your next letter guess? ")
        # How can we reorder words in the list to put it in right order?
    elif user_guess not in word_to_guess:
        print('Wrong guess. You have {} guesses remaining.'.format(guesses))
        user_guess = input("Guess again. ")
        guesses -= 1
        if guesses == 0:
            print('Game Over')
            break
