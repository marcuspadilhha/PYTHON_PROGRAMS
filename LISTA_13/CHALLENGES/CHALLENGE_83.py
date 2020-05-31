# enhancements
print("\033[1;35m","$"*50)
print(f"{'Validating mathematicians expressions': ^50}")
print("$"*50)
# statements
expression=[]
count1=count2=0
# library

# input
expression=input("\033[1;30mPlease input the expression:")

# processing
count1=expression.count('(')
count2=expression.count(')')



# output

if count1==count2:
    print("\033[1;33mValid expression, congratulations!")
elif count1>count2:
    print(f"\033[1;31mInvalid expression, missing {count1-count2} right parenthesis!")
elif count2>count1:
    print(f"\033[1;31mInvalid expression, missing {count2-count1} left parenthesis!")
