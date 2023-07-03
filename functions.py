def gpt():
    print("This is a function")


gpt()
gpt()
gpt()


def add():
    x = 60
    y = 30
    print("The sum is :", x + y)


add()


def product():
    x = float(input("First number"))
    y = float(input("Second number"))
    result = x * y
    print("Product is", result)


product()

# function that calculates average of a list #
numbers = [3,4,5,6,7,8,9]
def avg():
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    result = average
    print("Average is",result)


avg()

