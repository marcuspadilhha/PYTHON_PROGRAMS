guys=list()
data=list()
for person in range(0,3):
    data.append(str(input('Name: ')))
    data.append(int(input('Age: ')))
    guys.append(data[:])
    data.clear()

for being in guys:
    if being[1] >=18:
        print(f'{being[0]} is older')
    if being[1] < 18:
        print(f'{being[0]} is younger')
