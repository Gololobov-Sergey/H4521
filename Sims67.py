import random
class Human:
    def __init__(self, name, car=None, job=None):
        self.name = name
        self.house = House()
        self.car = car
        self.job = job
        self.money = 100

    def work(self):
        pass

    def shopping(self):
        self.money -= random.randint(1, 10)
        self.house.food += random.randint(1, 10)
        if self.car == None:
            print("Пішли на шопінг пішки")
        else:
            if self.car.drive(random.randint(1,10)):
                print("Поїхали на шопінг на авто")
            else:
                print("Пішли на шопінг пішки")


    def eat(self):
        pass

    def chill(self):
        pass

    def cleaning(self):
        pass

    def info(self):
        pass

    def live(self, day):
        pass

    def is_alive(self):
        return self.money > 0

class Car:
    def __init__(self, model):
        self.model = model
        self.fuel = 60    # l
        self.state = 100  # %

    def drive(self, length):
        rashid = length * 0.1
        if self.fuel - rashid > 0:
            print(f"Ми проїхали {length} км, витратили {rashid} л пального")
            self.fuel -= rashid
            self.state -= length * 0.01
            return True
        else:
            print("Подорож не можлива. Не вистачає пального")
            return False

    def add_fuel(self):
        pass

    def __str__(self):
        pass

class Job:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        pass


class House:
    def __init__(self):
        self.food = 0
        self.pollution = 0

    def __str__(self):
        pass
