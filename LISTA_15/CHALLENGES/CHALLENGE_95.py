# enhancements
print('\033[1;35m', end='')
print('%' * 60, '\033[1;3;33m')
print(f"{' Improving the dictionaries ':-^60}\033[m")
print('\033[1;35m', end='')
print('%' * 60)
# statements
data = {}
roster = []
goals = []
players = code = 0
# library

# input
print('\033[1;30m')
while True:
    data['name'] = input("Player's Name: ")
    players = +1
    data['match'] = int(input("How many matches did the player play? "))
    c = 0
    for c in range(1, data['match'] + 1):
        goal = int(input(f'How many goals did the player in the match {c}? '))
        goals.append(goal)
    data['result'] = goals[:]
    goals.clear()
    roster.append(data.copy())
    choice = input("Do yo want continue? [Y/N]? ").strip().upper()
    if choice == 'N':
        break
    print(' ')
print('\033[1;33m', end='')
print('-=' * 30)

# processing
print('')
print('\033[1;37m', end='')
print(f"{'cod': <5}{'Name': <15}{'Total': <10}  {'Goals': <30}")
print('\033[1;35m', end='')
print('-' * 60)

# output
for c in range(0, len(roster)):
    print(f"{c: <5}{roster[c]['name']: <15}  {sum(roster[c]['result']): <10}{roster[c]['result']}")
print('\033[1;33m', end='')


while True:
    print('-=' * 30)
    print('\033[1;30m')
    code = int((input('Do you want to know about what player? [Insert code] ')))
    if c < code:
        print('\033[1;31mInvalid number, please type a number again.')
        print('')
    elif code < 0:
        print('\033[1;31mInvalid number, please type a number again.')
        print('')
    else:
        print('\033[1;37m')
        print(f"Performance of {roster[code]['name']}:")
        print('\033[1;35m', end='')
        print('-' * 60)

        matches=len(roster[code]['result'])

        t=0
        for t in range(0, matches):
            print(f"In the game {t+1}, he made {roster[code]['result'][t]} goals.")
            t += 1

        print('\033[1;30m')
        choice=input('Do you want to know about another player? [Y/N]').upper().strip()
        print('')
        if choice == 'N':
            break
print('-=' * 30)
print('\033[1;30m')