class Nguoi:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def inputInfo(self):
        newName = input("Nhap ten: ")
        newAge = input("Nhap tuoi: ")
        newAddress = input("Nhap dia chi: ")
        self.name = newName
        self.age = newAge
        self.address = newAddress
    def printInfo(self):
        print("Thong tin: ", self.name, self.age, self.address)

class NhanVien(Nguoi):
    def __init__(self, name, age, address, salary, hourOfWork):
        super().__init__(name, age, address)
        self.salary = salary
        self.hourOfWork = hourOfWork
    def inputInfo(self):
        super().inputInfo()
        newSalary = int(input("Tien luong: "))
        newHourOfWork = int(input("So gio lam viec: "))
        self.salary = newSalary
        self.hourOfWork = newHourOfWork
    def printInfo(self):
        super().printInfo()
        print("Salary: ", self.salary)
        print("Hour of work: ", self.hourOfWork)
    def tinhThuong(self):
        bonus = 0
        if self.hourOfWork >= 200:
            bonus = self.salary * 0.2
        elif self.hourOfWork >= 100 and self.hourOfWork < 200:
            bonus = self.salary * 0.1
        else:
            bonus = 0
        print("Tien thuong: ",  bonus)

nv1 = NhanVien("Nguyen Van A", 20, "Ho Chi Minh", 1000000, 200)

nv1.inputInfo()

nv1.printInfo()

nv1.tinhThuong()