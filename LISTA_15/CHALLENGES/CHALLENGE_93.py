# enhancements
print('\033[1;33m', end='')
print('<<>>' * 15)
print(f"{'Register of Soccer Player':-^60}")
print('<<>>' * 15)
# statements
count = 0
results = []
data={}
# library

# input # processing
print('\033[1;30m')
data['name'] = input("Player's Name: ")
matches = int(input("How many matches does he play: "))
if matches == 0:
    print("\033[1;31mThe player didn't play any match.")
else:
    for count in range(1, matches+1):
        goals = int(input(f"How many goals did the player do in the match {count}? "))
        results.append(goals)
        count = +1
    data['goals']=results
    data['total']=sum(results)

# output
    print('\033[1;33m','-=-'*20)
    print('\033[1;34m',data)

    print('\033[1;33m', '-=-' * 20,'\033[1;37m')

    print(f"The camp name has the value {data['name']}")
    print(f"The camp goals has the values {results}")
    print(f"The camp total has the value {data['total']}")

    print('\033[1;33m', '-=-' * 20, '\033[1;36m')

    print(f"The soccer player {data['name']} has played {matches} matches. ")
    for p in range(1,matches+1):
        print(f"    => In the match {p}, he's made {results[p-1]} goals.")
    print(f"It was a total of the {sum(results)} goals.")
    print(f"It was a mean of {sum(results)/matches} goals per match.")