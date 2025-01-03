# Read input word
word = input().strip()

# Dictionary to store the frequency of each character
frequency = {}

# Calculate frequencies of each character
for char in word:
    frequency[char] = frequency.get(char, 0) + 1

# Set to track printed characters
printed = set()

# Build the output by traversing the word
result = ""
for char in word:
    if char not in printed:
        result += str(frequency[char])
        printed.add(char)

# Print the result
print(result)
