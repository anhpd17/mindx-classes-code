# a = 1
# b = 2

# print(a + b)
# print(a.__add__(b))
# print(a.__sub__(b))

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, number):
        self.x += number
        self.y += number
        return self
    def __str__(self):
        return f'{self.x} - {self.y}'


p1 = Point(1,1)
p1 += 1
print(p1)


# class Animal:
#     def __init__(self, numberOfLeg, sound):
#         self.numberOfLeg = numberOfLeg
#         self.sound = sound
#     def play_sound(self):
#         print(self.sound)

# class Dog(Animal):
#     def __init__(self, numberOfLeg, sound, name):
#         super().__init__(numberOfLeg, sound)
#         self.name = name
    
# d1 = Dog(4, "Go go", "Milu")
# d1.play_sound()


# class A:
#     def sayHello():
#         print("Hello world")

#     def intro():
#         print("I am a coder")

# class B(A):        
#     def age():
#         print("I am 20 years old")
#     # override
#     def sayHello():
#         a = 1
#         b = 2
#         print(a+b)
#         print("Goodbye world")

# p1 = B
# p1.sayHello()