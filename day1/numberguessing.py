from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_answer, turns):
    """Checks the user's guess against the actual answer and returns remaining turns."""
    if user_guess > actual_answer:
        print("Too high!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it right! The answer is {actual_answer}.")
        return 0

def set_difficulty():
    """Sets the difficulty level and returns the number of attempts."""
    difficulty = input("Choose a difficulty level: easy or hard: ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def guessing_game():
    """Main function to play the guessing game."""
    print("Welcome to the guessing game!")
    print("I am thinking of a number between 1 and 100.")

    answer = randint(1, 100)
    turns = set_difficulty()

    user_guess = 0
    while user_guess != answer and turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))

        turns = check_answer(user_guess, answer, turns)

        if turns == 0:
            if user_guess != answer:
                print(f"You've run out of guesses. The answer was {answer}.")
            break

guessing_game()
