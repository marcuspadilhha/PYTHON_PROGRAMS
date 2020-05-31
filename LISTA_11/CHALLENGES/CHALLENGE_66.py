# enhancements
print("\033[1;30m", "%%%" * 20, "\n", " " * 20, "Count and sum", "\n", "%%%" * 20)

# statements
num = count = sum = 0

# library

# input # processing
while True:
    num = int(input("\033[32;1mType the next number or 999 to stop: "))
    if num == 999:
        break
    count += 1
    sum += num

# output
print(f"\033[33;1mYou typed {count} numbers and the numbers' sum is {sum}")
