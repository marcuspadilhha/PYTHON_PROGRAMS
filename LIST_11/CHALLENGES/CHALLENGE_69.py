# enhancements
print("\033[1;35m", "@@@" * 23, "\n", " " * 20, "Registration of people", "\n", "@@@" * 23)
print(" ")

# statements
age = -1
sex = choise = " "
major = man = youngwoman = 0
# library

# input
while True:
    while True:
        age = int(input("\033[1;30mInput person's age: "))
        if -1<age<151:
            break

    while True:
        sex = input("Input person's sex: [M] Masculine, [F] Feminine").upper().strip()
        if sex in "MF":
            break

# processing
    if age > 17:
        major += 1
    if sex == "M":
        man += 1
    if sex == "F" and age < 18:
        youngwoman += 1

    choise = input("Do you want continue? [Y] Yes, [N] No").upper().strip()
    if choise == "N":
        break
    print(" ")

# output
print(f"\n\033[1;33mThere are {major} people above 18. ")
print(f"There are {man} men.")
print(f"There are {youngwoman} women below 18.")
