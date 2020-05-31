# enhancements
print('\033[1;30m', '¬' * 60)
print(f"{'Mega Sena Guesses': ^60}")
print('¬' * 60)
# statements
und = 1
group = list()
# library
import random

# input
number = int(input('\033[1;34mHow many games do you want me to draw? '))
print(' ')
# processing
for Guess in range(1, number + 1):
    for bet in range(1, 7):
        group.append(random.randint(1, 60))
    print(f'\033[1;33mGame {und}: {group[:]}')
    group.clear()
    und += 1
print(f"\n\033[1;32m{'Good luck!':=^60}")

# output
