"""
Program: Match Coins Game - Coin Class
Author: Jaylen Johnson
Purpose: Represents a single coin that can be tossed.
Starter code: No starter code was used.
Date: 6/28/2026
"""

import random

class Coin:
    """Represents a single coin."""

    def __init__(self):
        """Initialize the coin with a random starting side."""
        self.__sideup = random.choice(["Heads", "Tails"])

    def toss(self):
        """Randomly set the coin side to Heads or Tails."""
        toss_result = random.randint(0, 1)

        if toss_result == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Return the current side facing up."""
        return self.__sideup        