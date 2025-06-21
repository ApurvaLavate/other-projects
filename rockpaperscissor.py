import random

def rockpaperscissor():
    choices = ["rock", "paper", "scissors"]
    print("Welcome to the Rock, Paper, Scissors Game!")

    while True:
        user_choice = input("\nType your choice (rock, paper, or scissors): ").lower()

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue  

        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins! Better luck next time.")

        play_again = input("\nDo you want to play again? (yes or no): ").lower()

        if play_again in ["yes", "y"]:
            print("Let's play again!")
            continue
        elif play_again in ["no", "n"]:
            print("Thanks for playing! See you next time.")
            break
        else:
            print("Invalid input. Exiting the game.")
            break

rockpaperscissor()
