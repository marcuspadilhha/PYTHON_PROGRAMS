# enhancements
print('\033[1;33m', '&' * 60)
print(f"{' Dice Game ':-^60}")
print('&' * 60)

# statements
game = {}
ranking=()

# library
from random import randint
from time import sleep
from operator import itemgetter

# input


# processing
game={'gamer 1':randint(1,6),
      'gamer 2':randint(1,6),
      'gamer 3':randint(1,6),
      'gamer 4':randint(1,6),}
# output
print('\033[1;30m', end='')
print(f'{"Values Drawn": ^60}')

ranking = sorted(game.items(), key=itemgetter(1), reverse=True)

for k, v in game.items():
    print(f'                {k} took {v} at the dice.')
    sleep(1)

print('\033[1;31m')
print(f'{"Ranking of the gamers": ^60}')

for i, v in enumerate(ranking):
    print(f'                 {i+1}º place: {v[0]} with {v[1]}')
    sleep(1)



