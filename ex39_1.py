# items() method 
dic1 = {'A' : 'one', 'B' : 'two', 'C' : 'three', 'D' : 'four'}
print(dic1.items())
print(list(dic1.items()))
del dic1['A'] 
print(dic1.items())
# list() fuction
string = 'TURTLE SHALL TAKE OVER THIS WORLD'
x = list(string)
print(x)
tuple1 = ('A', 'B', 'C', 'D')
y = list(tuple1)
print(y)
z = list(dic1)
print(z)

# get() method

print(dic1.get('C'))
print(dic1.get('A', 'Nani'))
