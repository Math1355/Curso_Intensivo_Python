cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'audi'
print(car == 'bmw')

car = 'Audi'
print(car == 'audi')

car = 'Audi'
print(car.lower() == 'audi')
print(car)