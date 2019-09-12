# creates  function that take as many number
# of arguments(param)


def make_pizza(size, *toppings):
    '''Summarize the pizza we are about to make'''
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f'- {topping}')


def greeting(*name):
        print(f'Hello {name}')
