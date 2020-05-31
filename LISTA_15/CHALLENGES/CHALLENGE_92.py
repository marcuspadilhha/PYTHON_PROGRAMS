# enhancements
print('\033[1;36m',end='')
print("{[]}"*15)
print(f'{"Worker Registration":¨^60}')
print("{[]}"*15)
# statements
register={}
# library
from datetime import date

# input
print('\033[1;30m')
register['name']=input("Worker's Name: ")
register['year']=int(input("Worker's Birth's Year: "))
register['number']=int(input("Document's Number: [0 if it doesn't exist]"))
# processing # output
if register['number'] is not 0:
    register['hiring']=int(input('Year of hiring: '))
    register['wage']=float(input('Wage: [R$]'))
    print('\033[1;33m')
    print(f"The worke's name is {register['name']}.")
    print(f"He/She is {date.today().year - register['year']} years old.")
    print(f"His/her document value is {register['number']}.")
    print(f"He/She was hired at the year of {register['year']}.")
    print(f"His/Her wage is R$ {register['wage']}.")
    age=date.today().year - register['year']
    retire=(35-(date.today().year-register['hiring']))+age
    print(f"He/She will retire when he/she complete {retire} years old")
else:
    print('\033[1;33m')
    print(f"The worke's name is {register['name']}.")
    print(f"He/She is {date.today().year-register['year']} years old.")
    print(f"His/her document value is {register['number']}.")




