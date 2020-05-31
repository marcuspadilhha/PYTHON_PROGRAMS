# enhancements
print('\033[1;35m', '@' * 50)
print(f"{'More about matrices':^50}")
print('@' * 50)
# statements
matrix = [[0,0,0], [0,0,0], [0,0,0]]
even=list()
column3=list()
line2=list()
# library

# input
print('\033[1;32m')
for line in range(0, 3):
    for column in range(0, 3):
        matrix[line][column] = int(input(f'Type a number for the position [{line},{column}]: '))
        if matrix[line][column]%2==0:
            even.append(matrix[line][column])
        column3.append(matrix[line][2])
        line2.append(matrix[1][column])



# processing

# output
print('\033[1;34m')
for line in range(0,3):
    for column in range(0,3):
        print(f'[{matrix[line][column]:^5}]',end='')
    print()
print('\033[1;33m')
print(f'The list of even numbers was: {even}')
print(f'The sum of third column value is {sum(column3)}')
print(f'The biggest second line value is {max(line2)}')