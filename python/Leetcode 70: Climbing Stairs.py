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
