shopping_list = []
finished_shopping = 'Done'

print('What do you want to add to your shopping list?')
print('Enter done when you are finished shopping.')

while True:
    wanted_items = input().capitalize()
    if wanted_items == finished_shopping:
        print('Finished shopping.')
        for number, item in enumerate(sorted(shopping_list)):
            print('{0}: {1}'.format(number + 1, item))
    elif wanted_items not in shopping_list:
        print('Adding {} to the list.'.format(wanted_items))
        shopping_list.append(wanted_items)
        print(sorted(shopping_list))
    elif wanted_items in shopping_list:
        print('Removing {} from the list.'.format(wanted_items))
        shopping_list.remove(wanted_items)
        print(shopping_list)
