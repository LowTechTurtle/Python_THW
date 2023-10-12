#i =0
#numbers = []
## method 1
#while i<5:
#   print('at the top i is', i)
#   numbers.append(i)
#   i += 1
#   print(f'at the bottom i is {i}')
#print(' so in the end, i is', i, 'and we got this list', numbers)

##method 2
#numbers = []
#def fun(a, x, y):
#    print(f'at the top x is {x}')
#    if x<=a:
#        x += y
#        numbers.append(x)
#        print(f'at the bottom x is {x}')
#        print(f'and now the list is {numbers}')
#        return fun(a, x, y)
#    else:
#        print('the age of men is over, the orc will now rise to its peak')  
#        numbers.insert(0, 1)
#        print(f'and we got the list {numbers}')
        
#fun(5, 1, 1)
##method 3
x = 0
print(x)
numbers = []
for x in range(0, 5):
    print(f'first x is {x}')
    x += 3
    print(f'now x is {x}')
    numbers.append(x)
print(numbers)
print(x)


