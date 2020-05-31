# enhancements
print("\033[1;36m", "%" * 60)
print(f"{'Extracting data from a list': ^60}")
print("%" * 60, "\n")
# statements
list=[]
# library

# input
while True:
    num = input("\033[1;32mInput a number in the list or press [E] to exit:").upper().strip()

# processing
    if num=="E":
        break
    num=int(num)
    list.append(num)

# output
print(f"\n\033[1;33mIt was typed {len(list)} numbers")
print(sorted(list,reverse=True))
if 5 in list:
    print(f"\033[1;34mThe value 5 was typed and it is in the list")
else:
    print("\033[1;34mThe value 5 was not typed and it is not in the list.")