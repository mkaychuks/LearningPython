'''9-3. Users: Make a class called User . Create two attributes called
first_name and last_name , and then create several other attributes that are
typically stored in a user profile. Make a method called describe_user()
that prints a summary of the user’s information. Make another method called
greet_user() that prints a personalized greeting to the user.'''


class User:
    "usesr profile generation"

    def __init__(self, first_name, last_name, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = address

    def describe_user(self):
        print(f'This is your profile {self.first_name}')
        print(
            f"Surname: {self.last_name} \nage: {self.age} \naddress: {self.address}"
        )

me = User('achufusi', 'ifeanti', '15', 'chima lane')

me.describe_user()
