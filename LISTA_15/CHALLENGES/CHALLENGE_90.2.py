print('\033[1;33m','~'*60)
print(f'{"Dictionary in Python": ^60}')
print('~'*60)
mean=dict()
print('\033[1;30m')
mean['Name']=input('Name: ')
mean['Mean']=float(input(f'Mean of {mean["Name"]}: '))
if mean['Mean']<6:
    mean['Situation']='Reproved'
else:
    mean['Situation']='Approved'

print('\033[1;32m')
print(f"The person's name is {mean['Name']}.")
print(f"The person's mean is {mean['Mean']}")
print(f"Situation is {mean['Situation']}")
