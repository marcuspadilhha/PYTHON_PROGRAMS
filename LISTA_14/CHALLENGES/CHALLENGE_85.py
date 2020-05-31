# enhancements
print('\033[1;30m','=/='*20)
print(f"{'Lists with odds and evens': ^60}")
print('=/='*20)
print('\033[1;34m')
# statements
even=list()
odd=list()

# library

# input
for und in range(1,8):
    number=int(input(f'Type the {und}º of 7 numbers: ').strip())

# processing
    und+=1
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)

# output
print(f'\n\033[1;33mThe list of the even numbers is {sorted(even)}')
print(f'The list of the odd numbers is {sorted(odd)}')
