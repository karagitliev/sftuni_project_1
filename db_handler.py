import json

DATABASE = 'users.txt'


def read_user_data(param=None, req_type=None):
    with open(DATABASE) as f:
        data = json.load(f)

    resp = []
    for key, value in data.items():
        if req_type == 'all':
            resp.append(value)
        else:
            if req_type not in value:
                continue
            if value[req_type] == param:
                resp.append(value)

    if resp:
        return 'ok', resp
    else:
        return 'err', 'err'


def write_user_data(new_user, number):
    with open(DATABASE) as file:
        data = json.load(file)

    if number in data.keys():
        print(f'\nA contact with the number {number} already exists, would you like to update it?')

        update_options = '''\n-- Please choose an option --
1 - Yes
2 - No
'''
        print(update_options)

        update_options_items = {
            '1': 'Yes',
            '2': 'No'
        }

        usr_inp = input('Enter a number: ')
        while usr_inp not in update_options_items.keys():
            usr_inp = input('Please enter a valid number (1 or 2): ')

        if usr_inp == '1':
            data[number] = new_user
            print('\nUpdate successful!')
        else:
            print('\nNo changes were made!')
    else:
        data[number] = new_user
        print(f'\nNew entry added successfully!')

    with open(DATABASE, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def search_data(param, req_type, is_del=None):
    param = param.lower()

    status, result = read_user_data(param, req_type)
    text = ''
    if status == 'ok':
        sufix = ''
        count_results = len(result)
        if count_results > 1:
            sufix = 's'
        text += f'- {count_results} result{sufix} found -\n'
        text += '--------------------\n'

        nums = []
        for contact in result:
            if 'name' in contact:
                text += f"Name: {contact['name'].capitalize()}\n"
            if 'city' in contact:
                text += f"City: {contact['city'].capitalize()}\n"
            if is_del:
                nums.append(contact['number'])

            text += f"Number: {contact['number']}\n"
            text += '--------------------\n'

        if is_del:
            return text, nums

    elif is_del:
        return '- No valid entries found -\n', '0'
    else:
        text += '- No valid entries found -\n'

    return text


def delete_user_data(param, req_type):
    result, nums = search_data(param, req_type, 'delete')

    del_user = ''
    if req_type == 'number':
        if nums == '0':
            print(result)
            exit()
        print(f'Are you sure you want to delete the following user:\n')
        print(result)

        del_user = nums[0]
    else:
        print(result)
        while del_user == '':
            del_user = input('Enter the user Number from the list above you want to delete: ')

            if del_user not in nums:
                print(f'Invalid match with search criteria \'{param}\' and number \'{del_user}\'')
                exit()
            print(f'Are you sure you want to delete user with Number {del_user}?\n')

    choice = input('Y/n? ').lower()
    if choice == 'y':
        with open(DATABASE) as f:
            data = json.load(f)

            del data[del_user]

        with open(DATABASE, 'w') as outfile:
            json.dump(data, outfile, indent=4)

        print(f'User with Number {del_user} was successfully deleted.')
