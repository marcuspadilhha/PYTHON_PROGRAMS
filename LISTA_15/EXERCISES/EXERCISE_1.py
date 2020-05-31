print('')
people={'Name':'Marcus', 'Sex':'M', 'Age':'31'}
print(f'{people["Name"]} is {people["Age"]} years old. ')
print(people.keys())
print(people.values())
print(people.items())
print(' ')
for k in people.keys():
    print(k,end=' ')
print(' ')
for v in people.values():
    print(v, end=' ')
print('')
for k,v in people.items():
    print(k, v)
print(' ')
del people['Sex']
print(people)
print(' ')
people['Weight']='90'
print(people)