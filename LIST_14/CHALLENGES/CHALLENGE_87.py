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
even=list()
col3=list()

# library

# input # processing
for und in range(0, 3):
    number = int(input(f'Type a number for the position [0,{und}]: '))
    if number%2==0:
        even.append(number)
    if und==2:
        col3.append(number)
    list00.append(number)
    list0.append(list00[:])
    list00.clear()
number = und = 0

for und in range(0, 3):
    number = int(input(f'Type a number for the position [1,{und}]: '))
    if number%2==0:
        even.append(number)
    if und==2:
        col3.append(number)
    list11.append(number)
    list1.append(list11[:])
    list11.clear()
number = und = 0

for und in range(0, 3):
    number = int(input(f'Type a number for the position [2,{und}]: '))
    if number%2==0:
        even.append(number)
    if und==2:
        col3.append(number)
    list22.append(number)
    list2.append(list22[:])
    list22.clear()

# output
print('\033[1;33m')
print(list0[:])
print(list1[:])
print(list2[:])

print('\033[3;34m')

print(f'\033[3;34mThe sum of all even values is {sum(even)}')
print(f'\033[3;34mThe sum of all third column values is {sum(col3)}')
print(f'The biggest value of the second line is {max(list1[:])}')