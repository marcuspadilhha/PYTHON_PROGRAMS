# enhancements
print('\033[1;36m', end='')
print('#' * 50)
print(f"{' Join Dicts and Lists ':-^50}")
print('#' * 50)
# statements
data = dict()
roster = list()
ages = list()
number = women = 0

# library

# input
print('\033[1;30m')
while True:
    data['name'] = input('Name: ')
    number += 1
    while True:
        data['sex'] = input('Sex [M/F]: ').upper().strip()
        if 'M' in data['sex']:
            break
        if 'F' in data['sex']:
            women += 1
            break
        else:
            print('\033[1;31mPlease, type a valid value for sex.\033[1;30m')
    data['age'] = int(input('Age: '))
    roster.append(data.copy())
    out = input('Do you want insert more people? [Y/N]').upper().strip()
    if out == 'N':
        break
    print(' ')

# processing
c = 0
for c in range(0, number):
    ages.append(roster[c]['age'])
    c += 1
mean = (sum(ages)) / (len(ages))

# output
print('\033[1;33m')
print(f'The group has {number} people;')
print(f'The women recorded were {women};')
print(f'The mean of the ages is {mean};')
print('The people with age above the mean are:')
print('\033[1;34m')
c = 0
for c2 in roster:
    if roster[c]['age'] > mean:
        print(f"Name = {roster[c]['name']}, Sex = {roster[c]['sex']}, Age = {roster[c]['age']}")
    c += 1

