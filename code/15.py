def count_special_characters(s):
    count = 0
    for char in s:
        if not char.isalnum():  # Check if the character is not alphanumeric (not a letter or digit)
            count += 1
    return count

# Taking input from the user
str_input = input("Enter a string: ")
special_char_count = count_special_characters(str_input)
print(f"Count of special characters: {special_char_count}")
