def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    index = int((len(choices) * (hash(str(id(choices))) % 1)) % len(choices))
    return choices[index]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You won!")
    else:
        print("You lose!")

def play_game():
    user_score = 0
    computer_score =0

    while True:
        print("\n Rock-Paper-Scissors Game")
        print("Choose rock, paper or scissors. Type 'exit' to quit.")
        user_choice = input("Your choice: ").lower()

        if user_choice == "exit":
            print("\nThank you for playing!")
            print(f"Final Scores: You {user_score} - {computer_score} Computer")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice!")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_score)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        display_result(user_choice, computer_choice, winner)
        print(f"Score: You {user_score} - {computer_score} Computer")

if __name__ == "__main__":
    play_game()    