def count_consonants(sentence):
    # Define vowels for checking
    vowels = "aeiouAEIOU"
    consonant_count = 0

    # Loop through each character in the sentence
    for char in sentence:
        # Check if the character is an alphabet and not a vowel
        if char.isalpha() and char not in vowels:
            consonant_count += 1

    return consonant_count

# Taking input from the user
sentence = input("Enter a sentence: ")
consonant_count = count_consonants(sentence)
print(f"Number of consonants in the sentence: {consonant_count}")
