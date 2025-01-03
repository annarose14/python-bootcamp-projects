def count_words(sentence):
    # Split the sentence by spaces and filter out any empty words
    words = sentence.split()
    return len(words)

# Taking input from the user
sentence = input("Enter a sentence: ")
word_count = count_words(sentence)
print(f"Number of words in the sentence: {word_count}")
