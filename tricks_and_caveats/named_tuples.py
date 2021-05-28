from collections import namedtuple

# Declaring a tuple
Car = namedtuple('Car', [
    'color',
    'mileage'
])

car = Car('red', 10.5)

print(car)

# Unpacking a tuple
color, mileage = car
print(color)
print(mileage)

try:
    car.color = 'blue'
except AttributeError as err:
    print(err)

# Extending/Inheriting named tuple
# Extending methods


class CarWithMethods(Car):
    def mileage_in_kms(self):
        return self.mileage / 1.6


car_with_methods = CarWithMethods('green', 20)
print(car_with_methods.mileage_in_kms())

# Extending attributes
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
electric_car = ElectricCar('blue', 25.5, '10h')
print(electric_car)
