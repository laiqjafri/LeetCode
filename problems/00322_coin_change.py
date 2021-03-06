# 322. Coin Change
# Medium
#
# 6944
#
# 195
#
# Add to List
#
# Share
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
#
#
#
# Example 1:
#
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1
# Example 3:
#
# Input: coins = [1], amount = 0
# Output: 0
# Example 4:
#
# Input: coins = [1], amount = 1
# Output: 1
# Example 5:
#
# Input: coins = [1], amount = 2
# Output: 2
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int, memo=None) -> int:
        if memo is None:
            memo = {}
        elif amount in memo:
            return memo[amount]

        if amount == 0:
            return 0

        smallest_change = float("inf")

        for coin in coins:
            remainder = amount - coin
            if remainder >= 0:
                change = self.coinChange(coins, remainder, memo)
                if change >= 0:
                    smallest_change = min(smallest_change, change + 1)

        memo[amount] = -1 if smallest_change == float("inf") else smallest_change
        return memo[amount]
