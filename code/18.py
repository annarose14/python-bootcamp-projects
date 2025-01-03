def count_vowels(sentence):
    # Define vowels for checking
    vowels = "aeiouAEIOU"
    vowel_count = 0

    # Loop through each character in the sentence
    for char in sentence:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Taking input from the user
sentence = input("Enter a sentence: ")
vowel_count = count_vowels(sentence)
print(f"Number of vowels in the sentence: {vowel_count}")
