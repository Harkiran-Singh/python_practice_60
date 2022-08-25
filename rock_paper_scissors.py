import random
import sys

"""
rock beats scissors
scissors beats paper
paper beats rock
"""


def rsp():
    possible_choices = ['rock', 'paper', 'scissors']
    user_score = 0
    while user_score != -1:
        current_choice = random.choice(possible_choices)
        user_choice = input("Choose rock paper or scissors to play or quit to end the game\n")
        print(f"\nYour Choice {user_choice}")
        print(f"Opponent Choice {current_choice}")
        if user_choice in possible_choices:
            if user_choice != current_choice:
                if (user_choice == "rock" and current_choice == "scissors") or (
                        user_choice == "scissors" and current_choice == "paper") or (
                        user_choice == "paper" and current_choice == "rock"):
                    user_score = user_score + 1
                    print(f"You Win !! Your current score is {user_score}")
                else:
                    user_score = -1
                    print(f"{current_choice} beats {user_choice}")
            elif user_choice == current_choice:
                print("It's a Tie! Keep Playing\n")
        elif user_choice == "quit":
            break
        else:
            sys.exit("Not a valid choice, please choose rock, scissors or paper next time")
    sys.exit("Game Over")


def main():
    print("""Welcome to the Rock Scissors Paper Game\n
    rock beats scissors\n
    scissors beats paper\n
    paper beats rock\n
    """)
    rsp()


if __name__ == "__main__":
    main()
