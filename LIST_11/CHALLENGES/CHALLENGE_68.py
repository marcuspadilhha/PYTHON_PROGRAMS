# enhancements
print("\033[1;30m", "$#$" * 23, "\n", " " * 20, "Let's play even or odd!", "\n", "$#$" * 23)
# statements
person = computer = total = count = 0
choise = result = vexit = " "
# library
from random import randint
from time import sleep

# input # processing
while True:
    computer = randint(0, 10)
    choise = input("\033[1;345mSelect [E] for even or [O] for odd:").strip().upper()
    person = int(input("Type a number:"))

    total = computer + person

    if total % 2 == 0:
        result = "E"
    elif total % 2 != 0:
        result = "O"
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")
    sleep(0.5)
    print(".")

    if result == choise:
        print(f"\n\033[1;33mThe computer selected {computer} and the total was {total}. Congratulations, you've won!")
        count += 1

    elif result != choise:
        print(f"\n\033[1;31mThe computer selected {computer} and the total was {total}. You've lose!")

    vexit = input("\n\033[1;35mDo you want to continue? [Y - Yes, N - No]").strip().upper()
    if vexit == "N":
        break

    print("\033[1;30m")
    print("$#$" * 23)
# output
print("\033[1;30m")
print("$#$" * 23)
print(f"\nYou exited from the program and you won {count} times!")