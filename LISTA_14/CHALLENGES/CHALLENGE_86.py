# enhancements
print('\033[1;30m', '$' * 50)
print(f"{'Matrix on python': ^50}")
print('$' * 50)
print('\033[1;36m')
# statements
list0 = list()
list00 = list()
list1 = list()
list11 = list()
list2 = list()
list22 = list()

# library

# input # processing
for und in range(0, 3):
    number = int(input(f'Type a number for the position [0,{und}]: '))
    list00.append(number)
    list0.append(list00[:])
    list00.clear()
number = und = 0

for und in range(0, 3):
    number = int(input(f'Type a number for the position [1,{und}]: '))
    list11.append(number)
    list1.append(list11[:])
    list11.clear()
number = und = 0

for und in range(0, 3):
    number = int(input(f'Type a number for the position [2,{und}]: '))
    list22.append(number)
    list2.append(list22[:])
    list22.clear()

# output
print('\033[1;33m')
print(list0[:])
print(list1[:])
print(list2[:])
