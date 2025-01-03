# You are going to write a function 
# called calculate_love_score() that tests the compatibility between two names. 
def calculate_love_score(name1, name2):
    # Convert names to lowercase to make the function case-insensitive
    combined_names = (name1 + name2).lower()

    true_score = sum(combined_names.count(char) for char in "true")

    love_score = sum(combined_names.count(char) for char in "love")
    love_score_combined = int(f"{true_score}{love_score}")

  
    print(love_score_combined)


calculate_love_score("Angela Yu", "Jack Bauer")


