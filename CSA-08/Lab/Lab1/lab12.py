# Bai 1
# class Employee:
#     def __init__(self, name="Nguyen Van A", position="Nhan vien"):
#         self.name = name
#         self.position = position
#     def say_hi(self):
#         print("Hi, my name is", self.name)
#     def tell_position(self):
#         print("I am a", self.position)

# employee1 = Employee("PDA", "b")
# employee1.say_hi()
# employee1.tell_position()

# Bai 2
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
    def cal_P(self):
        print("P =", (self.height + self.width) * 2)
    def cal_S(self):
        print("S =", self.height * self.width)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def cal_P(self):
        print("P =", self.radius * 2 * 3.14)
    def cal_S(self):
        print("S =", self.radius * self.radius * 3.14)

shape_name = input("Type the name: ")
if(shape_name == "rectangle"):
    input_height = float(input("Height :"))
    input_width = float(input("Width :"))
    rec1 = Rectangle(input_height, input_width)
    rec1.cal_P()
    rec1.cal_S()
elif(shape_name == "circle"):
    input_radius = float(input("Radius :"))
    cir1 = Circle(input_radius)
    cir1.cal_P()
    cir1.cal_S()
else:
    print("Invalid")