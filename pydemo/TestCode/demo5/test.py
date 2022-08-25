class Person():
    __home = "world"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sleep(self, time):
        self.time = time
        print("name is", self.name, "age is", self.age, 
        "sleep time is", self.time, 
        "home is", Person.home)

    @classmethod
    def home(cls):
        return cls.__home

person = Person("tom", 18)

person.sleep(20)
print(person.home())
print(Person.home())