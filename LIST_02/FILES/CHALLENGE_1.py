#input
num1=int(input("\033[7;33mType the first number!\033[m"))
num2=int(input("\033[7;34mType the second number!\033[m"))

#processing
sum=num1+num2

#output
print("\033[1;33mThe sum between {} and {} is {}!\033[m".format(num1,num2,sum))
