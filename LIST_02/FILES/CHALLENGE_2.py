#input
obj=input("Input an object:")

#output
print("\033[7;1;33mNumber:",obj.isnumeric(),"\033[m")

print("\033[7;34mLetter:",obj.isalpha(),"\033[m")

print("\033[7;4;35mAlphanumeric:",obj.isalnum(),"\033[m")

print("\033[7;36mUppercase:",obj.isupper(),"\033[m")

print("\033[7;1;37mLowercase:",obj.islower(),"\033[m")

print("\033[7;4;30mTitle:",obj.istitle(),"\033[m")

print("\33[7;0;31mSpace:",obj.isspace()"\033[m")


