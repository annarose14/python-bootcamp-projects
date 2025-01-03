def encode_word(word):
    # Dictionary to store character frequencies
    freq = {}
    result = ""

    # Calculate the frequency of each character
    for char in word:
        freq[char] = freq.get(char, 0) + 1

    # Generate the result based on the first occurrence order
    for char in word:
        if char in freq:
            result += str(freq[char])
            del freq[char]  # Remove the character after processing its frequency

    return result


# Input and validation
word = input("Enter a word: ").strip().upper() 

if not word.isalpha() or not word.isupper():
    print("Error: Input must contain only uppercase English alphabets.")
elif any(word.count(char) > 9 for char in word):
    print("Error: No character should repeat more than nine times.")
else:
    print(encode_word(word))
