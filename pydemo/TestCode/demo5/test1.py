class Animals():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Bird(Animals):
    def __init__(self, name, age, skill):
        super(Bird, self).__init__(name, age)
        self.skill = skill

    def go(self):
        print(self.name, self.age, self.skill)


b = Bird("tom", "man", "fly")
b.go()