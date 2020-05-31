# enhancements
print('\033[1;37m', '%' * 60)
print(f"{'School Report': ^60}")
print('%' * 60)
# statements
namelist = list()
scorelist = list()
suballlist = list()
alllist = list()
qtd = 0
# library

# input
print('\033[1;34m')
while True:
    namelist.append(str(input('Name: ')))
    scorelist.append(float(input('Score1: ')))
    scorelist.append(float(input('Score2: ')))
    suballlist.append(namelist[:])
    suballlist.append(scorelist[:])
    alllist.append(suballlist[:])
    namelist.clear()
    scorelist.clear()
    suballlist.clear()
    qtd += 1
    choice = str(input('Do you want continue? ').strip().upper())
    if choice == 'N':
        break
# processing # output
print('\033[1;31m')
print(f"{'Name':^10}", end='')
print(f"{'Score':^10}")
for num in range(0, qtd):
    print(f"{alllist[num][0]}", end='')
    print(f'{sum(alllist[num][1]) / 2}')
print('\033[1;37m')
num = int(input("Who pupil do you want to show the score of?"))
print('\033[1;33m')
print(alllist[num][1])



