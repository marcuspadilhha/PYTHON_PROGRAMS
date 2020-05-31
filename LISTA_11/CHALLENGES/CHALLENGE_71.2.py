# enhancements
print("\033[1;37m")
print("=" * 30)
print("{:^30}".format("Cash Machine"))
print("=" * 30)
# statements
note = 50
totalnote = 0
# library

# input
value = int(input("\033[1;34mInput the value you want withdrawn:"))
total = value

# processing
while True:
    if total >= note:
        total -= note
        totalnote += 1
    else:
        if totalnote>0:
            print(f"\033[1;34mTotal of {totalnote} notes of \033[1;33m{note:.2f}")
        if note == 50:
            note = 20
        elif note == 20:
            note = 10
        elif note == 10:
            note = 1
        totalnote = 0
        if total == 0:
            break
