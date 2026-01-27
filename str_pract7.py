# Program to find length, number of vowels and consonants in a string

str1 = input("Enter a string: ")

length = len(str1)
vowels = 0
consonants = 0

for c in str1:
    ch = c.lower()   # convert to lowercase for easy comparison
    if 'a' <= ch <= 'z':   # only consider alphabetic characters
        if ch in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1
        else:
            consonants += 1

print("Length of string:", length)
print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
