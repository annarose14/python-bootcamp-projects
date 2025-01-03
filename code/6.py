# Take input from the user
sentence = input("Enter a sentence: ")

# Convert the sentence to lowercase and split into words
words = sentence.lower().split()

# Create a dictionary to count the occurrences of each word
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Find the word with the maximum frequency
max_word = None
max_count = 0

for word in words:  # Iterate through the original order
    if word_count[word] > max_count:
        max_word = word
        max_count = word_count[word]

# Print the result
print(max_word)
