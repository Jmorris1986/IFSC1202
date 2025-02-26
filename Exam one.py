# Import randint from the random library
from random import randint

# Prompt for the user's name
user_name = input("Enter your name: ")

# Set the user's score and computer score to zero
user_score = 0
computer_score = 0

# Play the game while the user's score is less than 30 and the computer's score is less than 30
while user_score < 30 and computer_score < 30:
    # Prompt the user to press the enter key
    input(f"{user_name}, press Enter to roll the dice...")

    # Set the user's roll to a random number between 1 and 6
    user_roll = randint(1, 6)
    print(f"{user_name} rolled: {user_roll}")

    # If the user's roll is 1, reset the user's score to 0 and print an "LOL Mistake" statement
    if user_roll == 1:
        user_score = 0
        print(f"LOL Mistake! {user_name}, your score is reset to 0.")
    else:
        user_score += user_roll

    # Set the computer's roll to a random number between 1 and 6
    computer_roll = randint(1, 6)
    print(f"The computer rolled: {computer_roll}")

    # If the computer's roll is 1, reset the computer's score to 0 and print an "LOL Mistake" statement
    if computer_roll == 1:
        computer_score = 0
        print("LOL Mistake! The computer's score is reset to 0.")
    else:
        computer_score += computer_roll

    # Print the current user score and current computer score
    print(f"Current Score: {user_name}: {user_score} | Computer: {computer_score}")
    print("-" * 40)

# When the game has ended, check who has the highest score and print the result
if user_score > computer_score:
    print(f"Congratulations {user_name}! You won with {user_score} points.")
else:
    print(f"Sorry {user_name}, the computer won with {computer_score} points.")
