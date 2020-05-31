#input
day=input('\033[7;30mWhat is the day of your birth?\033[m')
month=input('\033[7;33mWhat is the month of your birth?\033[m')
year=input('\033[7;36mWhat is the year of your birth?\033[m')

#output
print("Your birth's date is\033[1;30m", month,"\033[m\033[1;33m", day, "th\033[m,\033[1;36m",year,"\033[m")