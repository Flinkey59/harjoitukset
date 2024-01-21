import random 


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def tick_age(self):
        self.age += 1

        return self.age


people = [Person(i, random.randint(0, 40)) for i in range(100)] #the list people is NOT an object, this is the same as people = [] + append thingy

for h in range(100):
    people[h].tick_age()
    print(people[h].age)
