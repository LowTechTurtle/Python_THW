##inheritance

#base class
class Mammal:
    def __init__(self, name, age):
        self.__pri = 300
        self.name = name
        self.age = age
    att = 'We are warm-blooded'
    def eat(self):
        print(f'We usually eat till we\'re {age} years old and die')
        print(f'Because {age} is our average life span')
    def sleep(self, hours):
        print(f'We sleep {hours} hours a day')
    def printpriatt(self):
        print(self.__pri)
#derived class
class Dog(Mammal):
    def bark(self, times):
        print(f'We bark roughly about {times} a day')


doggo1 = Dog('husky', 5 )
print(doggo1.name)
print(doggo1.age)
doggo1.bark(123123)
doggo1.sleep(12)
print(doggo1.att)
mam1 = Mammal('turtle', 200)
print(mam1.att)
print(doggo1.att)
mam1.printpriatt()
mam1.__pri = 500
print(mam1.__pri)
mam1.printpriatt()
