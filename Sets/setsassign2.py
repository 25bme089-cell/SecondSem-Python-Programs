# Accept a paragraph
para = input("Enter a paragraph: ")

# Create set of unique words
words = set(para.split())
print("Unique words:", words)
print("Number of unique words:", len(words))

# Accept two sentences
s1 = set(input("Enter first sentence: ").split())
s2 = set(input("Enter second sentence: ").split())

# Find common words
common = s1.intersection(s2)
print("Common words:", common)
