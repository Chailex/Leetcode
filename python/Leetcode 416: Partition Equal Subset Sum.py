class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        odd_even = sum(nums) % 2
        target = sum(nums) // 2

        if odd_even == 1:
            return False
        
        dp = set()
        dp.add(0)

        for i in nums:
            new_dp = dp.copy()
            for j in dp:
                new_dp.add(j+i)
            new_dp.add(i)
            dp = new_dp
        
        return True if target in dp else False
