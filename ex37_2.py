from sys import exit
class turtle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        a = x*y
        print(a)
    def shit(x0, var2, var3):
        var = var2**var3 + var3**var2
        print(f"var is {var}")
        var2 += 1
        var = var2 ** var3 + var3**var2
        print(f'and now var is {var}')
    def __str__(self):
        return f"trying to understand class and {self.x}"


turtle1 = turtle(2, 7)
turtle1.shit(3, 6)
turtle2 = turtle(3,4)
turtle2.x = 5
turtle2.y = 7
print(turtle2.x, turtle2.y)


def funn():
    yield 1
    yield 2
    yield 3
banana = []
for i in funn():
    banana = banana + [i]
print(banana)

def morefun():
    i=1
    while True:
        a = i**i
        i += 1
        yield a
bananana = []
for m in morefun():
    if m > 100000:
        break
    else:
        bananana = bananana + [m]
        print(f'now bananana is {bananana}')
print(f'finally, bananana is {bananana}')

foo = 'tryna test something'
assert foo == 'tryna test something'
assert foo == 'trying to test something'
