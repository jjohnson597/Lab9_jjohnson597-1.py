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

main()