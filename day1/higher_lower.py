##DAY14
import data_higherlower
from data_higherlower import data
import random


A= random.choice(data)
B = random.choice(data)
while A == B:
    B = random.choice(data)

print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")
guess = input("Who has more followers? Type 'A' or 'B': ")

# Determine which option has more followers
if guess.lower() == 'a':
    if A['follower_count'] > B['follower_count']:
        print(f"Yay, {A['name']} has more followers!")
    elif A['follower_count'] < B['follower_count']:
        print(f"Sorry, {B['name']} has more followers!")
    else:
        print(f"It's a tie! Both have {A['follower_count']} followers.")
elif guess.lower() == 'b':
    if B['follower_count'] > A['follower_count']:
        print(f"Yay, {B['name']} has more followers!")
    elif B['follower_count'] < A['follower_count']:
        print(f"Sorry, {A['name']} has more followers!")
    else:
        print(f"It's a tie! Both have {B['follower_count']} followers.")
else:
    print("Invalid input! Please type 'A' or 'B'.")
# Provide feedback to the user