import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 30
        self.progress = 10
        self.energy = 50
        self.alive = True
        self.money = 50

    def study(self):
        print("Я пішов до академії IT STEP")
        self.energy -= 3
        self.progress += 1
        self.gladness -= 1

    def chill(self):
        print("Я пішов з друзяками гулять")
        self.gladness += 2
        self.energy -= 3
        self.progress -= 0.2

    def sleep(self):
        print("Я пішов спати")
        self.energy += 4
        self.gladness += 1


    def eat(self):
        print("Я смачно поїв")
        self.energy += 2
        self.gladness += 1
        self.progress -= 0.2

    def is_alive(self):
        if self.progress <= 0:
            print("В мене в голові одне сміття, життя не має сенсу")
            self.alive = False
        if self.gladness <= 0:
            print("В мене дипресія")
            self.alive = False
        if self.progress > 100:
            print("Я став академіком!")
        if self.energy <= 0:
            print("Я зовсім знесилений :(")
            self.alive = False


    def live(self, day):
        print(f"День №{day} з життя {self.name}")
        print("-"*30)

        func = [self.sleep, self.study, self.chill, self.eat]
        func[random.randint(0,3)]()

        # rnd = random.randint(1,4)
        # if rnd == 1:
        #     self.study()
        # elif rnd == 2:
        #     self.chill()
        # elif rnd == 3:
        #     self.sleep()
        # else:
        #     self.eat()

        self.info()
        self.is_alive()
        print()

    def info(self):
        print(f"На сьогодні {self.name} має:")
        print(f"Задоволення : {self.gladness}")
        print(f"Знання      : {self.progress}")
        print(f"Енергія     : {self.energy}")


student = Student("Vasya")
day = 1
while student.alive == True:
    student.live(day)
    day += 1