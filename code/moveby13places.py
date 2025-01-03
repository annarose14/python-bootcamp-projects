def rot13_transform(text):
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            char = char.upper()  # Convert to uppercase
            # Shift by 13 places, wrapping around using modulo
            new_char = chr(((ord(char) - 65 + 13) % 26) + 65)
            result += new_char
        else:
            result += char  # Keep non-alphabetic characters as-is
    return result

# Input
input_text = input("Enter the text: ")
# Transform and Output
output_text = rot13_transform(input_text)
print("Output:", output_text)
