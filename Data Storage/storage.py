# EXAMPLE 1

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)


# EXAMPLE 2

filename = 'numbers.json'

with open(filename) as f:
    numbers = json.load(f)

print(numbers)


# EXAMPLE 3
# storing a username in json format

username = input('What is your name? ')

filename = 'username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}")


# greeting an already registered username from the above json format

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back to the site, {username}")

# combining the code using try-except blocks


def get_stored_username():
    '''Get the stored username'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    '''Greet the user by name'''
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")
    else:
        username = input("What is your name? ")
        filename = "username.json"
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}")
