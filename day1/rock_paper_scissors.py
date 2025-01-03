# Rock paper Scissors
import random
print("Welcome to the game\n Let's play\n")
print("What do you choose\n")  
user_choice = int(input("Type 0 for Rock, Type 1 for paper and Type 2 for scissors\n"))

computer_choice = random.randint(0, 2)
print(f" Computer chose (computer_choice)")

if user_choice >= 3 or user_choice < 0:
 print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
 print("You win!") 

elif computer_choice == 0 and user_choice ==2:

 print("You lose!")

elif computer_choice > user_choice:

 print("You lose!")

elif user_choice > computer_choice:

 print("You win!")

elif computer_choice == user_choice:

 print("It's a draw!")


