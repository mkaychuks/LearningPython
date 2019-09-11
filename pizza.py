# creates  function that take as many number
# of arguments(param)


def make_pizza(*toppings):
    '''Summarize the pizza we are about to make'''
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f'- {topping}')

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')
