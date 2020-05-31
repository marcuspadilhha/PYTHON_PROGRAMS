# enhancements
print('\033[1;33m', '&' * 60)
print(f"{' Dice Game ':-^60}")
print('&' * 60)
# statements
game = {}
ranking={}
# library
from random import randint
from copy import deepcopy
#from operator import itemgetter

# input
print('\033[1;30m')
for p in range(1, 5):
    game['Name'] = input(f'Input the {p}° player name: ')
    game['Score'] = int(randint(1, 6))
    game['Score']=int(game['Score'])
    ranking[=game.copy()
    print(game['Score'])
    p+=1
# processing

print(ranking)
# output
