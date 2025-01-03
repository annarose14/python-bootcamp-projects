def rearrange_alphabetically(string):
    # Convert the string to lowercase for uniformity
    # Sort the characters in alphabetical order
    return ''.join(sorted(string.lower()))

# Example usage:
input_string = str(input())
result = rearrange_alphabetically(input_string)
print(result) 