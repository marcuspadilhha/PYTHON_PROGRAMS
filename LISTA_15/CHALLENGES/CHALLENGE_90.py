# enhancements
print('\033[1;30m', '&' * 60)
print(f'{"Dictionary in Python":^60}')
print('&' * 60)
# statements
data = dict()
result = ''
# library

# input
print('\033[1;34m')
data['name'] = str(input('Input the name of the pupil: '))
data['media'] = float(input('Input the media of the pupil: '))
# processing
if 0 < data['media'] < 5:
    result = 'Reproved'
elif 5 <= data['media'] < 7:
    result = 'in Recuperation'
elif 7 <= data['media'] <= 10:
    result = 'Approved'

# output
print(f'\033[1;33mThe name of the pupil is {data["name"]};')
print(f'The media of the pupil is {data["media"]};')
print(f'The pupil is {result};')