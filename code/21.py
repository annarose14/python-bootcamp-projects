def print_frequencies(s):
    freq_map = {}  # Dictionary to store frequencies
    printed = set()  # Set to track characters that have been printed

    # Count frequencies
    for char in s:
        if char in freq_map:
            freq_map[char] += 1
        else:
            freq_map[char] = 1

    # Print frequencies in the order of appearance
    for char in s:
        if char not in printed:
            print(freq_map[char], end=" ")  # Print the frequency
            printed.add(char)  # Mark character as printed

# Example usage
input_string = input("Enter a string: ")
print_frequencies(input_string)
