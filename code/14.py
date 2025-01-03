def longest_substring_without_repeating(s):
    char_index = {}  # Dictionary to store the last index of each character
    start = 0  # Start of the window
    max_length = 0  # Length of the longest substring

    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1  # Move start to the right of the last occurrence
        
        char_index[s[end]] = end  # Update the last index of the character
        max_length = max(max_length, end - start + 1)  # Update max length

    return max_length


# Taking input from the user
str_input = input("Enter a string: ")
length = longest_substring_without_repeating(str_input)
print(f"Length of the longest substring without repeating characters: {length}")
