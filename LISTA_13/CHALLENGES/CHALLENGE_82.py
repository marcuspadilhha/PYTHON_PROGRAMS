# enhancements
print("\033[1;30m", "#" * 40)
print(f"{'Dividing values in several lists': ^40}")
print('#' * 40)
# statements
listtotal = []
listeven = []
listodd = []

# library

# input
while True:
    num = (input("\033[1;3;34mPlease, Input a number or [E] to exit:")).strip().upper()

    # processing
    if num == "E":
        break

    num = int(num)

    listtotal.append(num)

    if num % 2 == 0:
        listeven.append(num)

    elif num % 2 != 0:
       listodd.append(num)

# output
print(f"\033[1;33mTotal list: {listtotal}")
print(f"Even list: {listeven}")
print(f"Odd list: {listodd}")
