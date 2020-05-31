#input
num1=input('\033[7;37mInput the first number:\033[m')
num2=input('\033[7;32mInput the second number:\033[m')

#processing
joint=num1+num2
print("\033[4;37m",joint,"\033[m")

num1=int(num1)
num2=int(num2)
sum=num1+num2
print("\033[4;32m",sum,"\033[m")
