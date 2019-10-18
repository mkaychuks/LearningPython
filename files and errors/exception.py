# EXAMPLE 1

try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide using integer 0")


# EXAMPLE 2
print('Give me two numbers, and I will divide them')
print("Enter 'q' to quit")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)


# EXAMPLE 3
'''Handling the FileNotFoundError Exception'''
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist")
else:
    # Count the approxiamte number of words in the file.
    words = contents.split()
    number_of_words = len(words)
    print(f"The file {filename} has about {number_of_words} words")


# EXAMPLE 4
'''Working with multiple files'''
# creating a function to handling FileNotFoundError Exception


def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f'Sorry, the file {filename} does not exist.')
        ## the following PASS statement makes the programme run without
        ## showing the user the output of the error..
        pass
    else:
        words = contents.split()
        number_of_words = len(words)
        print(f'The file {filename} has about {number_of_words} words')


filename = 'alice.txt'
count_words(filename)


filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'siddhartha.txt']

for file in filenames:
    count_words(file)


# TASK...
'''10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int , you’ll get a ValueError . Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.'''

while True:
    num1 = input('Enter first  number ')
    num2 = input('Enter second number ')
    try:
        sum = int(num1) + int(num2)
        print(sum)
        break
    except ValueError:
        print('Please enter an integer')
