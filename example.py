from sys import argv
script, file = argv
f=open(file)
print('ima print the whole file')
print(f.read())
f.seek(0)
print('ima print line1 and line2 and.. and so on')
print(f.readline())
print(f)
print(f.readline(), end='')
print(f)
print(f.readline(), end='')
print(f)
