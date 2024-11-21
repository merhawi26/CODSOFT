######################################## Task 4: ROCK PAPER SCISSOR GAME #####################################
import random

ROCK = "r"
SCISSOR = "s"
PAPER = "p"


def display():
    print(f"{20*'='} ROCK PAPER SCISSORS GAME {20*'='}")
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Rules:")
    print(" # Rock beats Scissors")
    print(" # Scissors beats Paper")
    print(" # Paper beats Rock")
    print("\nEnter your choice:")
    print(" # ROCK 🪨: 'r'")
    print(" # PAPER 📄: 'p'")
    print(" # SCISSOR ✂️: 's'")
    print("\nLet's play!\n")


def get_winner(player, computer):
    if (
        (player == ROCK and computer == SCISSOR)
        or (player == SCISSOR and computer == PAPER)
        or (player == PAPER and computer == ROCK)
    ):
        return "player"
    elif player == computer:
        return "The game is tie"
    else:
        return "computer"


def game():
    player_wins_counter = 0
    computer_wins_counter = 0
    game_tie_counter = 0
    while True:
        player = input("Your choice (r/p/s): ").lower()
        if not player in [ROCK, SCISSOR, PAPER]:
            print("Wrong value inserted! Try again")
            continue
        else:
            computer_choice = random.choice([ROCK, PAPER, SCISSOR])
            result = get_winner(player, computer_choice)
            if result == "player":
                player_wins_counter += 1

                print(
                    f"\n🎉 You WIN this round! You chose {player} 🆚 Computer chose {computer_choice}."
                )

            elif result == "computer":
                computer_wins_counter += 1
                print(
                    f"\n💻 Computer WINS this round! You chose {player} 🆚 Computer chose {computer_choice}."
                )

            else:
                game_tie_counter += 1

                print(f"\n🤝 It's a TIE! Both chose {player}.")

                print(
                    f"\n📊 SCORE: You: {player_wins_counter} | Computer: {computer_wins_counter} | Ties: {game_tie_counter}\n"
                )
            next_try = input("Continue? y/n\n").lower()
            if next_try != "y":
                print("Thanks for playing")
                print(
                    f"Final Score: You: {player_wins_counter} | Computer: {computer_wins_counter} | Ties: {game_tie_counter}"
                )
                break


if __name__ == "__main__":
    display()
    game()
