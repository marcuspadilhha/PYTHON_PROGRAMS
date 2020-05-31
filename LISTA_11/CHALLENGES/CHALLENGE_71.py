# enhancements
print("\033[1;37m", "~~~" * 20, "\n", " " * 20, "Cash Machine", "\n", "~~~" * 20)
print(" ")
# statements
value = 0
note100=note50 = note20 = note10 = note1 = 0
rnote100=rnote50 = rnote20 = rnote10 = rnote1 = 0
choise=" "

# library

while True:
    # input
    value = int(input("\033[1;30m Value to withdrawn: $"))

    # processing
    note100=value//100
    rnote100=value%100

    note50=rnote100//50
    rnote50=rnote100%50

    note20=rnote50//20
    rnote20=rnote50%20

    note10=rnote20//10
    rnote10=rnote20%10

    note1=rnote10

    # output

    print("\033[1;33m")
    if note100>0:
        print(f"Total of {note100} notes of $100,00")
    if note50>0:
        print(f"Total of {note50} notes of $50,00")
    if note20>0:
        print(f"Total of {note20} notes of $20,00")
    if note10 > 0:
        print(f"Total of {note10} notes of $10,00")
    if note1 > 0:
        print(f"Total of {note1} notes of $1,00")

    choise=input("\n\033[1;31mDo you want to continue? [Y/N]").strip().upper()
    if choise=="N":
        break
    print(" ")

print("\n\033[1;34mCome back often! Have a nice day!")

