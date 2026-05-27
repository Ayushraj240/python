import random
def get_choice():
 player_choice = input("Enter a choice (rock,paper,scissors): ")
 options = ["rock","scissors","paper"]
 computer_choice = random.choice(options)
 choices = {"player": player_choice , "computer": computer_choice}


 return choices

def check_win(player, computer):
    print(f"you chose {player}, computer chose {computer}")

    if player == computer:
        return "it's a tie"
    elif player == "rock" and computer == "scissors":
        return "player wins"
    elif player == "scissors" and computer == "rock":
        return "computer wins"
    elif player == "paper" and computer == "rock":
        return "player wins"
    elif player == "rock" and computer == "paper":
        return "computer wins"
    elif player == "scissors" and computer == "paper":
        return "player wins"
    elif player == "paper" and computer == "scissors":
        return "computer wins"

choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)