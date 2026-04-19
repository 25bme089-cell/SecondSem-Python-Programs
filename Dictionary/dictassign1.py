# Program to count word frequency in a string
text = input("Enter a string: ")

# Split string into words
words = text.split()

# Create dictionary for word frequencies
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Display dictionary
print("Word Frequency Dictionary:", freq)

# Find the maximum frequency
max_freq = max(freq.values())

# Display most frequent words
most_frequent = [word for word, count in freq.items() if count == max_freq]
print("Most Frequent Words:", most_frequent)
