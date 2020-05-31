# enhancements
print("\033[1;30m", "@@" * 125)
print("{:^230}".format("Brazilian Championship's Placement"))
print("\033[1;30m", "@@" * 125, "\n")
# statements
Teams = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo', 'Internacional', 'Corinthians',
    'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético Mineiro', 'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro',
    'CSA', 'Chapecoense', 'Avai')
# library

# input

# processing

# output
print("\033[1;34mList:")
print(f"\033[1;36m{Teams}")
print(f"\n\033[1;34mThe top five: \033[1;33m{Teams[0:5]}")
print(f"\n\033[1;34mThe last four placed: \033[1;31m{Teams[-4:]}")
print("\n\033[1;34mSorted List:")
print(f"\033[1;37m{sorted(Teams)}")
print(f"\n\033[1;34mGoiás's Position:\033[1;32m {Teams.index('Goiás')+1}º place")



