# enhancements
print("\033[1;32m","***"*15)
print(f"{'Vowels in the words': ^45}")
print("\033[1;32m","***"*15)
# statements
words=("Learn", "Programming", "Language", "Python", "Course", "Free", "Study", "Practice",
       "Work", "Market", "Programmer", "Future")
# library

# input

# processing
print("\033[1;34m")
for word in words:
    print(f"The word {word.upper()} has the vowels: ",end="")
    for vowels in word:
        if vowels in "aeiou":
            print(vowels,end=" ")
    print(" ")


# output

