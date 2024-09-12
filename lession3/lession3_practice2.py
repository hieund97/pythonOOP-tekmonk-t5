class Person():

    def __init__(self, year):
        self.year = year

    @property
    def age(self):
        if self.year is not None:
            return 2024 - self.year
        else:
            print("Năm sinh đang không có giá trị phù hợp")

    @age.setter
    def age(self, value):
        self.year = value

    @age.deleter
    def age(self):
        self.year = None


person = Person(2000)
person.age = 2001

del person.age
print(person.age)
