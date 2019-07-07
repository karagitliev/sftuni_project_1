import os
from sys import exit
import db_handler as db

os.system('clear')


def main_menu():
    menu = '''Please choose an option from the menu
-------------------------------------

1 - Search by Name
2 - Search by City
3 - Search by Number
4 - View all Entries
5 - Add new Entry
6 - Delete Entry

7 - Quit
'''

    print(menu)

    menu_items = {
        '1': search_by_name,
        '2': search_by_city,
        '3': search_by_number,
        '4': view_all_entries,
        '5': add_new_entry,
        '6': delete_entry,
        '7': exit,
    }

    usr_choice = input('Enter a menu number: ')
    while usr_choice not in menu_items.keys():
        usr_choice = input('Please enter a valid menu number (1 through 7): ')

    menu_items[usr_choice]()


def search_by_name():
    print('\n-- Search by Name --')

    choice = input('Please enter a name: ')
    resp = db.search_data(choice, 'name')
    print(resp)


def search_by_city():
    print('\n-- Search by City --')

    choice = input('Please enter a City: ')
    resp = db.search_data(choice, 'city')
    print(resp)


def search_by_number():
    print('\n-- Search by Number --')

    choice = ''
    while choice == '':
        choice = input('Please enter a valid Number: ')

    resp = db.search_data(choice, 'number')
    print(resp)


def view_all_entries():
    print('\n-- View all Entries --')

    resp = db.search_data('all', 'all')
    print(resp)

    return_to_menu()


def add_new_entry():
    new_user = {}

    print('\n-- Add new entry --')

    name = input('Please enter the Name: ')
    city = input('Please enter the City: ')
    number = input('Please enter the Number: ')

    new_user['name'] = name
    new_user['city'] = city
    new_user['number'] = number

    while new_user['number'] == '':
        new_user['number'] = input('Please enter a valid Number: ')

    db.write_user_data(new_user, number)
    return_to_menu()


def delete_entry():
    print('\n-- Delete Entry --')

    criteria = ''
    del_criteria = ['name', 'city', 'number']

    while criteria not in del_criteria:
        criteria = input(
            'Please enter delete criteria(name, city or number): ').lower().replace(' ', '')

    param = input(f'Please enter the {criteria}: ').lower()
    db.delete_user_data(param, criteria)
    return_to_menu()


def return_to_menu():
    print('\nReturn to Menu or Quit')

    action_options = '''\n-- Please choose an option -- :

-------------------------------------

1 - Return
2 - Quit
'''
    print(action_options)

    action_options_items = {
        '1': "Return",
        '2': "Quit"
    }

    usr_pick = input('Enter a number: ')
    while usr_pick not in action_options_items.keys():
        usr_pick = input('Please enter a valid number (1 or 2): ')

    if usr_pick == "1":
        main_menu()
    else:
        exit(0)


main_menu()
