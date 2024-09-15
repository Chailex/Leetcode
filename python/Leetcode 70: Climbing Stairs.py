# Solution using dictionary
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = dict()
        dp[1] = 1
        dp[2] = 2

        if n <3:
            return n

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
# Solution using constant space
class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = 1
        prev2 = 2

        if n <3:
            return n

        for i in range(3, n+1):
            temp = prev1 + prev2
            prev1 = prev2
            prev2 = temp
        
        return prev2
