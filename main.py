
class Student:
    count = 0
    def __init__(self, name, age, height=150):
        self.height = height
        self.name = name
        self.age = age
        #print(f"Hello, i am {self.name}")
        Student.count += 1

    def __str__(self):
        return (f"Мене звати {self.name}\n" +
                f"Мій зріст {self.height} см\n" +
                f"Вік {self.age} років\n")

    def grow(self, to_height=1):
        if self.height + to_height < 190:
            self.height += to_height

    def to_growup(self):
        if self.age < 55:
            self.age += 1




print(Student.count)

st = Student("Vasya", 15)
st.grow(10)
print(st)

st.to_growup()
print(st)

print(Student.count)

st1 = Student("Petya", 16, 155)
print(st)

print(Student.count)