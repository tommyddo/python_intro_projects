print("Fill in the {} with your chosen word based on the "
      "part of speech given to complete the sentence below.")
print()

print('Please excuse {name} who is far too {adjective} to attend {noun} class.')
name = input('Please excuse {}... (Enter a name) ').capitalize()
# How can we define a function that accounts for if the user inputs a different
# part of speech or data type for the variables of name, adjective and noun.
print("Please excuse {} who is far too {} to attend {} class."
      .format(name, {}, {}))
print()

adjective = input('...who is far too {}... (Enter an adjective) ')
print('Please excuse {} who is far too {} to attend {} class.'
      .format(name, adjective, {}))
print()

noun = input('...to attend {} class. (Enter a noun) ').capitalize()
print('Please excuse {} who is far too {} to attend {} class.'
      .format(name, adjective, noun))
