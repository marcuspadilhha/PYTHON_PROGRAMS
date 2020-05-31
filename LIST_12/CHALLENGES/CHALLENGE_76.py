# enhancements
print("\033[1;30m", "---" * 19)
print("{: ^54}".format("LISTAGEM DE PREÇOS"))
print("---" * 19)

# statements
count = counteven = countodd = 0
list = ('Pen', '$ 1,75', 'Erase', '$ 2,00', 'Notebook', '$ 15,00', 'Case', '$ 25,00', 'Protractor', '$4,20', 'Compass',
        '$ 9.99', 'Backpack', '$120,32', 'Pencils', '22,30', 'Book', '34,90')
# library

# input
for count in range(0,len(list)):
    if count % 2 == 0:
        print(f"{list[count]:.<50}",end=" ")
    else:
        print(list[count])
print("---" * 19)

