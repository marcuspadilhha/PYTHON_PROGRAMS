# enhancements
print('\033[1;37m', '%' * 60)
print(f"{'School Report': ^60}")
print('%' * 60)
# statements
file=list()
# library

# input
print('\033[1;34m')
while True:
    name=input('Name: ')
    grade1=float(input('Grade1: '))
    grade2 = float(input('Grade2: '))

# processing
    mean = (grade1 + grade2) / 2
    file.append([name,[grade1,grade2],mean])
    choice=input('Do you want to continue? ').strip().upper()
    if choice == 'N':
        break
# output
print('\033[1;30m','=-'*30)
print(f"{'Nº':<8}{'Name':<10}{'Mean':>8}")
print('-'*60)
for i, a in enumerate(file):
    print(f"{i:<8}{a[0]:<10}{a[2]:>8}")
print('\033[1;33m')
while True:
    num = int(input("Who pupil do you want to show the score of? [999 to exit]"))
    if num==999:
        break
    if num <= len(file)-1:
        print(f'The grades of the {file[num][0]} is {file[num][1]}')
print("Do come back!")