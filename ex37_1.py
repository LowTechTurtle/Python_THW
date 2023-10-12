#from sys import argv
#script, file = argv
turtle = 'turtle'
try: 
    print(turtlee)
except:
    print(turtle * 5)
else:
    print('that\'s lot of turtle')
finally:
    print('tawtle')
print('now we\'re gonna do sth new')
#raise MemoryError('Amnesia')
try:
    f=open(file)
except:
    print('that wasnt good')
finally:
    try:
        f.close()
    except:
        print('cant open that file')
print('bubala')
### the part up there was all about exception

###this is about with-as statement
x = input('Your file name pls: ')
with open(x, 'a+') as file:
    file.write('bubala')

