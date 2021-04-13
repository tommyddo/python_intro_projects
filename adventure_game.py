# This is an adventure in which the user will get to pick their own paths.

#define a new function to check if the user entered a string
def isString(user_input):
    try:
        var = int(user_input)
        return False
    except:
        try:
            var = float(user_input)
            return False
        except:
            return True

# def isInstanceOf(user_input, outType):
#     #
#     try:
#         if outType == 'int':
#             var = int(user_input)
#             return True
#     except:
#         try:
#             var = float(user_input)
#             return False
#         except:
#             return True
name = ''
# while True:
#     name = input('What is your name adventurer? ')
#     try:
#         val = int(name)
#         print('Please enter a real name')
#     except:
#         print('Welcome {}. Are you ready to begin your adventure? '.format(name))
#         break
name = input('What is your name adventurer? ')

isUserInputString = isString(name)

while not isUserInputString:
    print('Please enter a real name')
    name = input('What is your name adventurer? ')

print('Welcome {}. Are you ready to begin your adventure? '.format(name))

# while isinstance(name, int):
#     print('Please enter a real name')
#     name = input('What is your name adventurer? ')
# print('Welcome {}. Are you ready to begin your adventure? '.format(name))
user_answer = input('yes or no? ')
ranswer = 'yes'
wanswer = 'no'
exit = 'quit'
fanswer = 'forest'
banswer = 'beach'
approach1 = 'approach'
run1 = 'run'
if user_answer == ranswer:
    print("{}, you reach a fork in the road and see two paths. "
          "One leads to a forest and the other to the beach. "
          "Which path do you choose? ".format(name))
    user_answer = (input('Forest or beach? '))
    if user_answer == fanswer:
        print("You stumble along the forest and you see a bear. "
              "Do you approach it or run away?")
        user_answer = (input('Approach or run? '))
        if user_answer == approach1:
            print('hsad')
            #always printing apprach response?
        elif user_answer == run1:
            print('qqqqq')
    if user_answer == banswer:
        print("You walk along the beach and see a fin poking out the water. "
              "Do you investigate?")
        user_answer=(input('yes or no? '))
        if user_answer == ranswer:
            print('user entered ' + ranswer)
        elif user_answer == wanswer:
            print('user entered ' + wanswer)
            #always printing yes response?
    elif user_answer == exit:
        print('End Game')
elif user_answer == wanswer:
    print('{}, you need courage in your life. Until next time.'.format(name))
elif user_answer == exit:
    print('End Game')
