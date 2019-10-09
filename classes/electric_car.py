# handling inheritance


class Car:
    """A simple attempt to repressent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fuel = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the mileage"""
        print(
            f'this car has {self.odometer_reading} miles on it'
        )

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can"t roll the odometer back')

    def fill_gas_tank(self):
        if gas <= self.fuel:
            print("Refill")
        else:
            print(f'This car has a {self.fuel}-litre engine')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    '''A simple attempt to model a battery for an electric car'''

    def __init__(self, battery_size=75):
        '''Initialize the battery's attributes'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size'''
        print(f"This car had a {self.battery_size}-kWh battery")

    def get_range(self):
        '''Print a statement about the range this battery provides'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on full charge")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model S', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.battery_size = 100
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
