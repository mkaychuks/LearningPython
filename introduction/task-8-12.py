''' Sandwiches: Write a function that accepts a list of items
a person wants on a sandwich. The function should have one
parameter that collects as many items as the function call provides,
and it should print a summary of the sandwich that’s being ordered.
Call the function three times, using a different number of arguments
each time.'''


def sandwich(*flavor):
    print("\nThe following flavour(s) have been ordered for this sandwich")
    print(f'- {flavor}')

sandwich('Egg')
sandwich('Egg', 'Butter')
sandwich('egg', 'butter', 'jam')
