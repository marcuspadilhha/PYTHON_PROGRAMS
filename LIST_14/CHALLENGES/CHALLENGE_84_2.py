# enhancements
print('\033[1;30m', '#' * 60)
print(f'{"Composed list and data anlysis": ^60}')
print('#' * 60)
# statements
temp = []
group = []
under = over = 0
# library

# input
print('')
while True:
    name = str(input("\033[1;34mInput the person's name or press [E] to exit: ")).strip().capitalize()
    if name == 'E':
        break
    weight = float(input("Input the person's weight in kilos: "))
    # processing
    temp.append(name)
    temp.append(weight)
    if len(group) == 0:
        under = over = temp[1]
    else:
        if temp[1] > over:
            over = temp[1]
        if temp[1] < under:
            under = temp[1]
    group.append(temp[:])
    temp.clear()

# output
print(f'\n\033[1;32mIt has been registered {len(group)} people ')

print(f'The biggest weight was {over} and it belonged to:', end='')
for being in group:
    if being[1] == over:
        print(f'[{being[0]}]', end='')
print()
print(f'The smallest weight was {under} and it belonged to:', end='')
for being in group:
    if being[1] == under:
        print(f'[{being[0]}]', end='')
