class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Initialize the dp array with a value greater than the maximum possible (amount + 1)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: to make amount 0, we need 0 coins
        
        # Fill dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is still the initialized value i.e (amount+1), it means it's not possible to make the amount
        if dp[amount] != amount+1:
            return dp[amount]
        else:
            return -1
