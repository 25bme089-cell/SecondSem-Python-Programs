# Program to convert numbers 0 to 19 into words

words = ["zero","one","two","three","four","five","six","seven","eight","nine",
         "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
         "seventeen","eighteen","nineteen"]

num = int(input("Enter a number (0-19): "))

if 0 <= num <= 19:
    print("Word:", words[num])
else:
    print("Number out of range")
