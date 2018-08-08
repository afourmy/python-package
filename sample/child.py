from sample.person import Person


class Child(Person):

    def __init__(self, name, age, parent1, parent2):
        super().__init__(name, age)
        self.parent1 = parent1
        self.parent2 = parent2
