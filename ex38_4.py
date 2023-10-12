class animal:
    def eat(self):
        print('I can eat and shit')

class turtle(animal):
    def eat(self):
        super().eat()
        print('I can eat and shit and code too')

tur1 = turtle()
tur1.eat()
