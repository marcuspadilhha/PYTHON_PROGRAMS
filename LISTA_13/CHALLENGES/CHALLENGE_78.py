# enhancements
print("\033[1;30m","%"*50)
print(f"{'Numbers analyzing': ^50}")
print("%"*50)
# statements
list=[]
# library

# input
while True:
    num=input("\033[1;34mInput a number or press [E] to exit:").upper().strip()
# processing
    if num=='E':
        break
    elif num in '1234567890':
        num=int(num)
        list.append(num)
    else:
        print("\033[1;31mError")

# output
print(f"\n\033[1;33mThe biggest number is {max(list)} and it is in the {list.index(max(list))+1} position.")
print(f"The smallest number is {min(list)} and it is in the {list.index(min(list))+1} position.")