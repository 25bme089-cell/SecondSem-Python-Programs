def ispangram(z):
    ch=("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if z in ch:
        print("pangram")
    else:
        print("not pangram")
    return 0

str1=input("Enter string:")
c=ispangram(str1)
