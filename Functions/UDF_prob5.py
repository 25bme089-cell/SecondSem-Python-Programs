def ispangram(z):
    z = z.lower()
    
    if set("abcdefghijklmnopqrstuvwxyz").issubset(set(z)):
        print("pangram")
    else:
        print("not pangram")


str1 = input("Enter string: ")
ispangram(str1)
