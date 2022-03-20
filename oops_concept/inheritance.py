class animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def join(self):
        return f"{self.name} is {self.type}"

    def colour(self, shade):
        return f"{self.name} is {shade}"


class elephant(animal):
    pass


class bluewhale(animal):
    pass


class parrot(animal):
    pass


baby_elephant = elephant("ELephant", "vegetarian")
print(baby_elephant.join())
print(baby_elephant.colour("black"))
