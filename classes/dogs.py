# working with classes


class Dog:
    """ A simple dog characteristics """

    def __init__(self, name, age):
        """ Initializes name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate the dog is sitting down"""
        print(
            f'{self.name} is sitting down'
        )

    def roll_over(self):
        """Simulate a rolling over skit """
        print(
            f'{self.name} learnt how to rollover at {self.age} years old'
        )

my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()
