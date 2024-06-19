# create a simple rock,paper,scissors game
# provide a welcome message
# get the user's choice
# get the computer's choice
# compare the two choices
# print the results
# ask the user if they want to play again
# say goodbye at the end of the game
# use one function for the game logic

import random

def game(user_choice, play_again, computer_choice=None):
    # If computer_choice is None, generate a random choice
    if computer_choice is None:
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
    user_choice = user_choice.lower()
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "You win!"
    elif user_choice == "paper" and computer_choice == "rock":
        result = "You win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "You win!"
    else:
        result = "You lose!"
    return result, play_again

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Enter rock, paper, or scissors: ")
    play_again = input("Do you want to play again? (yes/no): ")
    result, play_again = game(user_choice, play_again)
    print(f"The result is: {result}")
    if play_again == "yes":
        play_game()
    else:
        print("Goodbye!")
