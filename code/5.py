# Take input from the user
sentence = input("Enter a sentence: ")

# Dictionary to store the frequency of first characters
char_count = {}

# Split the sentence into words and process each word
for word in sentence.split():
    first_char = word[0]  # Get the first character of the word
    char_count[first_char] = char_count.get(first_char, 0) + 1  # Update the count

# Find the character with the highest frequency
max_char = max(char_count, key=char_count.get)

# Output the result
print(f"The highest occurring first character is: '{max_char}'")
