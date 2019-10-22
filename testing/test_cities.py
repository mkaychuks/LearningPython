'''Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country , such as Santiago, Chile . Store the function in a module called
city _functions.py.
Create a file called test_cities.py that tests the function you just wrote
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run
test_cities.py, and make sure test_city_country() passes.'''

import unittest
from city_functions import formatted_city_name


class cityTestCase(unittest.TestCase):

    def test_city_country(self):
        name = formatted_city_name('lagos', 'nigeria')
        self.assertEqual(name, 'Lagos, Nigeria')

    def test_city_country_population(self):
        fullname = formatted_city_name('lagos', 'nigeria', 'population=1.5M')
        self.assertEqual(fullname, 'Lagos, Nigeria - Population=1.5M')


if __name__ == "__main__":
    unittest.main()
