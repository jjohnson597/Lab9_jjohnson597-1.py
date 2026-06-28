"""
Program: Match Coins Game - Player Class
Author: Jaylen Johnson
Purpose: Represents a player with a name, wallet, and coin object.
Starter code: No starter code was used.
Date: 6/28/2026
"""

from coin import Coin

class Player:
    """Represents a player in the Match Coins game."""

    def __init__(self, name):
        """Initialize the player with a name, wallet, and coin."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()
    
    def toss_coin(self):
        """Tell the player's coin to toss itself."""
        self.__coin.toss()
    
    def get_coin_side(self):
        """Return the side currently showing on the player's coin."""
        return self.__coin.get_sideup()
    