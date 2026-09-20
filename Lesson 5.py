class Human:
    def __init__(self):
        self.__heigth = 160
        self.__progress = 0

    def info(self):
        print("H", self.__heigth)
        print("P", self.__progress)

    def eat1(self):
        print("eat1")


    def set_height(self, h):
        if h < 200:
            self.__heigth = h

class Student(Human):
    # progress = 100
    def study(self):
        print("I`m study")



class Worker(Human):
    progress = 10


# h = Human()
# # print(h.heigth)
# # print(h.progress)
# h.set_height(170)
# h.eat1()
# #h.eat2()
# #h.eat3()

# s = Student()
# s.set_height(180)
# s.info()
# s.study()


class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 128
    def calculate(self):
        print("Calculating...")

class Display:
    def __init__(self):
        super().__init__()
        self.resolution = "4k"
    def display(self):
        print("Display screen...")


class SmartPhone(Display, Computer):
    def info(self):
        print(self.resolution)
        print(self.memory)


phone = SmartPhone()
phone.calculate()
phone.display()
phone.info()