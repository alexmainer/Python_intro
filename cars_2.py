class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(self.name, self.age, self.gender)


obj = People("DANIELLE", 19, "Male")
obj.display()
obj = People("SENJE", 16, "FeMale")
obj.display()
