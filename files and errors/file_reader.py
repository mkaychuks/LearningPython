filename = "pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

# for line in lines:
#    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()

print('is your birthday in pi'.upper())
print("______________________________")

birthday = input('Enter your birthday in this format mmddyy: ')

while True:
    if birthday in pi_string:
        print('Your birthday appears in the first million digits of pi')
        break
    else:
        print(
            'Your birthday does not appear in the first million digits of pi'
        )
