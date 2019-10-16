filename = 'programming.txt'

with open(filename, 'w') as writter:
    writter.write('I love programming\n')

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")


# TASK 1
'''Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.'''

nickName = input('What is your nickname? ')

fileName = 'guest.txt'

with open(fileName, 'w') as assign:
    assign.write(f'Your username has been stored as {nickName}')


# TASK 2
'''Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.'''

while True:
    print('Hello customer!!! ')
    username = input('What is your username please? ')

    usersFile = 'guest_book.txt'

    with open(usersFile, 'a') as database:
        database.write(f"{username} is already added\n")


# TASK 3
''' Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.'''


while True:
    print('Programming poll')
    answer = input('Why do you like programming? ')

    storageFile = 'poll_result.txt'

    with open(storageFile, 'a') as storageBase:
        storageBase.write(f'{answer} \n')
