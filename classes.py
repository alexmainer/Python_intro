class Cars:
    def __init__(self, model_name, name, engine,turbo, color, year):
        self.model = model_name
        self.name = name
        self.engine = engine
        self.turbo = turbo
        self.color = color
        self.year = year

    def display(self):
        print(self.model, self.name, self.engine, self.turbo, self.color, self.year)


# create an object

obj = Cars("AUDI","RS7","3000CC","TWIN TURBO", "Red", 2023)
obj.display()

obj = Cars("Merc","GLE", "4700CC" ,"Super-charger", "Green",1990)
obj.display()
