"""


https://leetcode.com/problems/coin-change/

ou are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104


"""


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        """
        Indea is to create DP araay to store the minimum number of coints required to get the given amount

        dp[i] : stores the minimum number of coins required to build the value amount i

        """

        dp = [float("inf")] * (amount + 1)  # 3 initalize the DP array with all infinity
        dp[0] = 0  ## the index=0 will be 0

        for target, val in enumerate(
                dp):  ## i stand for the amount. Calculate the minimum number of coins required to form the value i
            for coin in coins:
                if target - coin >= 0:  ## if the value of the coint is less than equal to the target, then to get the target value with the coins
                    dp[target] = min(dp[target], dp[target - coin] + 1)

        ## the last value at the dp array returns the minimum numer of coins required

        if dp[-1] == float("inf"):
            return -1
        return dp[-1]
