# enhancements
print("\033[1;30m", "%" * 50)
print(f"{'Ordered Numbers': ^50}")
print("%" * 50, "\n")
# statements
list = []

# library

# input
for c in range(0, 5):
    n = int(input("\033[1;34mType a value:"))
    # processing
    if c == 0 or n > list[-1]:
        list.append(n)
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos, n)
                break
            pos += 1
print(f"\n\033[1;33mThe values typed in order were {list}")

# output
