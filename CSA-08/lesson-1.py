class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def increaseAge(self, amount):
        self.age += amount
    def changeName(self, newName):
        self.name = newName
    def changeGender(self, newGender):
        self.gender = newGender

p1 = Person("PDA", 12, 1)

p1.changeName("PDB")
p1.increaseAge()
p1.changeGender(2)



person_list = []
person_data = {"name": "PDA", "age": 20, "gender": "male"}
for i in range(1, 10):
    p1 = Person(person_data["name"], person_data["age"], person_data["gender"])
    person_list.append(p1)

for person in person_list:
    print(person.name)
    print(person.age)
    print(person.gender)
    


# Bai tap thuc hanh 1
class Counter:
    def __init__(self):
        self.count = 0
    def tick(self):
        self.count += 1
    def reset(self):
        self.count = 0

c1 = Counter()
print(c1.count)

c1.tick()
c1.tick()
c1.tick()
c1.tick()

print(c1.count)

c1.reset()
print(c1.count)

    