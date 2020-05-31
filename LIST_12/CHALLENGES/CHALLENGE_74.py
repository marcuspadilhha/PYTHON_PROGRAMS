# enhancements
print("\033[1;30m")
print("#"*30)
print("{: ^30}".format('Random Numbers'))
print("#"*30)
# statements

# library
from random import randint

# input

# processing

# output
numbers = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

print(f"\n\033[1;34mDrawn numbers:{numbers}")
print(f"\033[1;31mSmaller number:{min(numbers)}")
print(f"\033[1;32mMean's numbers:{sum(numbers)/len(numbers)}")
print(f"\033[1;33mBigger number:{max(numbers)}","\033[1;30m")

