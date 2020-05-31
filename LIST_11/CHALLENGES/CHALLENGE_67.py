# enhancements
print("\033[1;30m", "~^~" * 25, "\n", " " * 30, "Taboo", "\n", "~^~" * 25, "\n")
# statements
num = count = start = end = 0
# library

# input
while True:
    num = input(
        "\033[1;34mDo you want to see the taboo what value with? [Press 'E' to exit from the program]").strip().upper()

    if num == "E":
        break
    num = int(num)

    start = int(input("What is the first number you want multiply?"))
    end = int(input("What is the last number you want multiply?"))

    for count in range(start, end + 1):
        print("\033[1;33m", f"{num} x {count} = {num*count}")
    print("\n\033[1;30m", "~^~" * 25,"\n")

print("\n\033[1;31mYou've exited from the program.")