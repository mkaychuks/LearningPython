'''Cars: Write a function that stores information about a car in a diction-
ary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the func-
tion with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this
one:

car = make_car('subaru', 'outback', color='blue', tow_package=True)'''


def car_info(manufacturer, model_name, **kwargs):
    """information about a car totally"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model_name'] = model_name
    return kwargs


my_car = car_info('Toyota', 'Camry', transmission='Manual',
                  year_of_production='2001', Drivers_license='Present',
                  Age_of_driver='23', Occupation_of_driver='Student',
                  Town_of_origin='Akwaeze')

print(my_car)
