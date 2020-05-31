# enhancements
print('\033[1;30m', '%' * 60)
print(f'{"Compound List Analysis": ^60}')
print('%' * 60)
# statements

# library
temp = list()
group = list()
under = over = 0
smallest = biggest = " "

# input
while True:
    name = str(input("\033[1;32mInput the person's name or press [E]: ")).upper().strip()
    if name == 'E':
        break
    weight = float(input("Input the person's weight: "))
    # processing
    temp.append(name)
    temp.append(weight)
    if len(group) == 0:
        under = over = temp[1]
    else:
        if temp[1] < under:
            under = temp[1]
            smallest = temp[0]
        if temp[1] > over:
            over = temp[1]
            biggest = temp[0]
    group.append(temp[:])
    temp.clear()

# output
print(f'\033[1;34mIt has been registered {len(group)} people.')

print(f'The biggest weight at the group is {over} and belongs to {biggest}')

print(f'The smallest weight in the group is {under} and belongs to {smallest}')
