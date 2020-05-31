# enhancements
print('\033[1;30m', '$' * 30)
print(f"{'Matrix in Python': ^30}")
print('$' * 30)
# statements
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# library

# input # processing
print('\033[1;34m')
for line in range(0, 3):
    for column in range(0, 3):
        matrix[l][c] = float(input(f'Type a value for [{l},{c}]: '))

# output
print('\033[1;33m')
print('=-' * 15)
for line in range(0, 3):
    for column in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()
