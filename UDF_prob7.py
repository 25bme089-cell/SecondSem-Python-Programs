def ispalindrome(s):
    s = s.lower()          # ignore case
    s = s.replace(" ", "") # remove spaces
    return s == s[::-1]

str1 = input("Enter a string: ")

if ispalindrome(str1):
    print("palindrome")
else:
    print("not palindrome")
