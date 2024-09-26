class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        maxlength = 0
        count = 0
        prefix = {0:-1}

        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in prefix.keys():
                maxlength = max(maxlength, i - prefix[count])
            else:
                prefix[count] = i
        
        return maxlength
