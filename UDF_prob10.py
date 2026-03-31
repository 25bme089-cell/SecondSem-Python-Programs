def word_frequency(text):
    words = text.split()
    freq = {}

    # Count frequency
    for word in words:
        word = word.lower()  # normalize case
        freq[word] = freq.get(word, 0) + 1

    # Sort dictionary by words
    sorted_freq = dict(sorted(freq.items()))

    return sorted_freq


# Example usage
sample = input("Enter string: ")
output = word_frequency(sample)
print(output)
