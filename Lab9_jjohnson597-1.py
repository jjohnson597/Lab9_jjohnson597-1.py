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
main()