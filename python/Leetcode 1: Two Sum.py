class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}  # Hash map to store the value and its index
        
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the complement
            
            # If the complement is already in the map, return the indices
            if complement in num_map:
                return [num_map[complement], i]
            
            # Otherwise, store the current number and its index in the map
            num_map[num] = i
