# list datastructures, its ordered and changeable
cars = ["Mercedes", "Lexus", "Toyota", "Audi"]
print(cars)
cars[1] = "subaru"
print(cars)
cars.append("Honda")
print(cars)
cars.insert(3, "volks")
print(cars)
cars.pop(0)
print(cars)
cars.sort(reverse=True)
print(cars)
cars.copy()
print(cars)
# this is a tuple,ordered but unchangeable
fruits = ("Mangoes", "Oranges", "Pineapple", "Avocado")
print(fruits)
for x in fruits:
    print(x)

# sets datastructures

countries = {"Kenya", "Uganda", "burundi", "chad", "egypt"}
print(countries)

# dictionaries
audi = {"amount": 5000000, "name": "Rs7", "color": "Red", "Engine": "3000 CC", "sixe": "Large"}
print(audi)
