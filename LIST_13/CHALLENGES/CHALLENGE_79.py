# enhancements
print("\033[1;30m", "%" * 50)
print(f"{'Numbers analyzing': ^50}")
print("%" * 50,"\n")
# statements
list = []

# library

# input
while True:
    num = input("\033[1;36mInput a number or press [E] to exit:").upper().strip()

    # processing
    if num == "E":
        break
    elif num not in '1234567890':
        print("\033[1;31mError")
    else:
        num = int(num)
        if num not in list:
            list.append(num)


# output
print(f"\033[1;33mYou have typed the values {sorted(list)}")
