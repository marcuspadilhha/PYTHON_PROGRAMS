# enhancements
print("\033[1;36m", "###" * 23,)
print("{::^70}".format("Registration of products"))
print("###" * 23)
print(" ")

# statements
name = choice = nameleast = " "
price = least = total = above1000 = count = 0
# library

# input
while True:
    name = input("\033[1;32mProduct's Name: ").upper().strip()
    price = float(input("Product's Price: $"))

    # processing
    total += price
    count += 1

    print(count)

    if price > 1000:
        above1000 += 1

    if count == 1:
        least = price
        nameleast = name

    if count > 1:
        if price < least:
            least = price
            nameleast = name

    choice = input("\033[1;3;37mDo you want to continue?").upper().strip()
    if choice == "N":
        break
    print(" ")
# output
print(f"\n\033[1;34mThe total in-store purchases was ${total:.2f}")
print(f"There are {above1000} products costing more than $1000.00")
print(f"The cheapest product was the {nameleast} and cost ${least:.2f}")
