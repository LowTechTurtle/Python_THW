class polygon:
    def __init__(self, sides):
        self.sides = sides
    def enter_sides(self):
        self.side = [ float(input(f'Enter the length of side {x}: '))  for x in range(1, self.sides+1) ]
    def print_sides(self):
        for i in range(1, len(self.side)+1):
            #a = i - 1
            print(f'Side {i} is {self.side[i-1]}')


class triangle(polygon):
    def __init__(self):
        polygon.__init__(self, 3)
    def find_area(self):
        a, b, c = self.side
        p = (a+b+c)/2
        area = ((p-a)*(p-b)*(p-c)*p)**(1/2)
        print(f'Area of this triangle is {area}')

tri1 = triangle()
tri1.enter_sides()
tri1.print_sides()
tri1.find_area()




