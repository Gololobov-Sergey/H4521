class Animal:
    def __init__(self, name):
        self.__name = name

class Mammals(Animal):
    pass

class Cat(Mammals):
    pass

class Dog(Mammals):
    pass

class Fish(Animal):
    pass

class GoldFish(Fish):
    pass
