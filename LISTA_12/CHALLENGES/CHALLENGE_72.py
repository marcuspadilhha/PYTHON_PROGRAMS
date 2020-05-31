# enhancements
print("\033[1;30m","%%%"*15)
print("{:^45}".format("Writen numbers"))
print("\033[1;30m","%%%"*15)
# statements

# library

# input
while True:
    num=int(input("\033[1;34mInput a  number from 0 to 20:"))

    while num<0 or num>20:
        num=int(input("\033[1;31mInput a correct number from o to 20:"))

    # processing
    numbers = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
               'nine', 'ten', 'eleven', 'twelve','thirteen', 'fourteen', 'fifteen',
               'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')
    # output
    print(f"\033[1;33mYou've typed the number {numbers[num]}")

    choice=input("\033[37;1mDo you want continue? [Y/N]").strip().upper()
    if choice == "N":
        break
    print(" ")