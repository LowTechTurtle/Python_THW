stuff = '1 2 3 4 5 6'
more = '7 8 9 10 11 12'
ten_num = stuff.split()
more_list = more.split()
print('Ten num is: ', ten_num)
print('Wait that was not ten numbers')

#while len(ten_num) <=10 :
for i in range(len(ten_num), 11):
    i += 1
    x = more_list.pop(0)
    ten_num.append(x)
    print('Now ten_num list has', len(ten_num), 'numbers')

print('Whoopsie, that was 11 num, gotta pop 1 out')
ten_num.pop()
print(ten_num)
print('Okay, now ten_num has 10 numbers')


print('Ima trying something now')
print(ten_num[-1])
print('banana'.join(ten_num))
print('paple'.join(ten_num[3:5]))
print(ten_num)
print(ten_num[3:5])
