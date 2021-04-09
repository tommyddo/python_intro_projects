# Mad Libs Game 1
print("Fill in the ____ with your chosen word "
      "based on the part of speech given.")
print()
print('Please excuse ____ who is far too ____ to attend ____ class.')
print()
name=input('Please excuse ____ ' 'Enter a name ')
print("Please excuse {} who is far too ____ to attend ____ class."
      .format(name))
print()
adjective=input('who is far too ---- ' 'Enter an adjective ')
print('Please excuse {} who is far too {} to attend ____ class.'
      .format(name,adjective))
print()
noun=input('to attend ____ class. ' 'Enter a noun ')
print("Please excuse {} who is far too {} to attend {} class."
      .format(name,adjective,noun))

