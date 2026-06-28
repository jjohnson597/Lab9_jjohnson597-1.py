"""
Program: Match Coins Game
Author: Jaylen Johnson
Purpose: Runs a two-player coin matching game using Player objects.
Starter code: No starter code was used.
Date: 6/28/2026
"""

from player import Player

def main():
    """Run the Match Coins game."""
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")
    
    play_again = "y"
    
    while play_again.lower() == "y":
        play_again = input("\nDo you want to toss the coins? (y/n): ")
        if play_again.lower() != "y":
            break

        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()
        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()
        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")
                
        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"...It's a Match! {player1.get_name()} wins a coin.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print(f"...No Match! {player2.get_name()} wins a coin.")
            print(f"\n{player1.get_name()} has {player1.get_wallet()} coins.")
            print(f"{player2.get_name()} has {player2.get_wallet()} coins.")
        
            print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} wins the game!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} wins the game!")
    else:
        print("It's a draw!")
main()