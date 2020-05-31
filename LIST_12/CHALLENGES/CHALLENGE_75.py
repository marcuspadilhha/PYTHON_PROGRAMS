# enhancements
print("\033[1;30m","#"*30)
print("{: ^30}".format("Numbers Analyse"))
print("#"*30)
print(" ")
# statements
count = count1 = count2 = 0
# library

# input
n1 = int(input("\033[1;34mInput first number: "))
n2 = int(input("Input second number: "))
n3 = int(input("Input third number: "))
n4 = int(input("Input fourth number: "))
group = (n1, n2, n3, n4)

# processing
for count in group:
    if count == 9:
        count1 += 1

for count in group:
    if count % 2 == 0:
        count2 += 1

# output
print(f"\033[1;33mThe number 9 appears {count1} times ")
if 3 in group:
    print(f"The value 3 appears at the {group.index(3)+1}º position ")
print(f"The even numbers appear {count2} times")