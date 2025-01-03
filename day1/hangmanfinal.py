import random
from hangman_words import word_list
from hangman_art import stages, logo

# Initial settings
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
correct_letters = []

# Display initial placeholders
placeholder = "_" * word_length
print(logo)
print(f"{' '.join(placeholder)}")

game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    # Check if letter was already guessed
    if guess in correct_letters:
        print(f"You've already guessed {guess}.")
    else:
        correct_letters.append(guess)

        # Update the display for correct guesses
        display = ""
        for letter in chosen_word:
            if letter in correct_letters:
                display += letter
            else:
                display += "_"
        
        print(f"{' '.join(display)}")

        # Check if the guessed letter is not in the word
        if guess not in chosen_word:
            lives -= 1
            print(f"Your guessed letter '{guess}' is not in the word. You lose a life.")
            print(stages[lives])
            if lives == 0:
                game_over = True
                print("You Lose.")
                print(f"The correct word was '{chosen_word}'.")
        
        # Check if the player has won
        if "_" not in display:
            game_over = True
            print("You Win!")

