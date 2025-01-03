word = input("Enter the word: ")  # Take input from the user

# Create a dictionary to store the frequency of each character
frequency = {}

for char in word:  # Count the frequency of each character
    if char not in frequency:
        frequency[char] = 1
    else:
        frequency[char] += 1

result = ""  # String to store the output
for char in word:  # Use the first occurrence order
    if char in frequency:
        result += str(frequency[char])
        frequency.pop(char)  # Remove the character to ensure it's processed only once

print(result)  # Print the final encoded string
