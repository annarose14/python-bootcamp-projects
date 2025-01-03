# Input the string
text = input("Enter a string: ")

# Split the string into words
words = text.split()

# Use a dictionary to count the frequency of each word
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Find the word with the maximum frequency
most_frequent_word = max(word_count, key=word_count.get)

# Output the result
print("Most frequent word:", most_frequent_word)
