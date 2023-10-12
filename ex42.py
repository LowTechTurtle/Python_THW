class fish:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    att = 'we have gill'

class salmon(fish):
    def __init__(self, tail):
        super().__init__(tail, 18)
        nani = 'what was that'
        self.tail = tail

#x = salmon('long tail')
#print(x.name)
#print(x.age)
#print(x.tail)
###

class A:
    def age(self):
        print("Age is 21")
class B:
    def age(self):
        print("Age is 23")
class C(B, A):
    def age(self):
        super().age()
class D(A, B):
    def age(self):
        super().age()
#c = C()
#c.age()
#d = D()
#d.age()

#B.age(d)
