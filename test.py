class class1:
    def __init__(self, obj):
        self.obj = obj
    def x(self):
        a = self.obj.y()
        print(a)
class class2:
    def y(self):
        print('this is y from class2')
        return 'death'
m = class2()

n = class1(m)

n.x()
