class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError()

    def look(self):
        raise NotImplementedError()


class Dog(Animal):
    def speak(self):
        print("barks")

    def look(self):
        print("black")


class Cat(Animal):
    def speak(self):
        print("purr")

    def look(self):
        print("orange")


dog = Dog("jil")
print(dog.name)
dog.speak()
dog.look()
cat = Cat("GIP")
cat.speak()
print(cat.name)
