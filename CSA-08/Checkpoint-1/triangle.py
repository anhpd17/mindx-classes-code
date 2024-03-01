class Triangle:
    # Tam giác có 3 cạnh là a, b, c
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    # Phương thức lấy được kiểu của tam giác
    def getType(self):
        if self.a == self.b and self.b == self.c:
            print("Type: Tam giac deu!")
        elif self.a == self.b or self.a == self.c or self.b == self.c:
            print("Type: Tam giac can!")
        else:
            print("Type: Tam giac thuong!")
    # Phương thức tính chu vi tam giác
    def getPerimeter(self):
        print("Chu vi tam giac: ", self.a + self.b + self.c)

t1 = Triangle(3, 3, 3)

t1.getType()

t1.getPerimeter() 