class something():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def banana(self):
        self.a = int(self.x)*int(self.y)
class thatthing():
    def start(self):
        print('im deducting this shit')
        obj.a -= 1
        print(obj.a)

obj = something(3, 4)
obj.banana()
print(obj.a)

thatthing().start()

obj.banana()

print(obj.a)
 
obj.x = 4
obj.y = 7
print('after')
print(obj.a)
obj.banana()
print(obj.a)

