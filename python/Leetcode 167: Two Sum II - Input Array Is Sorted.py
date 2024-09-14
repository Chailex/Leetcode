class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left, right = 0, len(numbers) - 1  # Initialize two pointers
        
        while left < right:
            current_sum = numbers[left] + numbers[right]  # Calculate the sum
            
            if current_sum == target:
                return [left + 1, right + 1]  # Return 1-based indices
            
            elif current_sum < target:
                left += 1  # Move the left pointer to the right to increase the sum
            
            else:
                right -= 1  # Move the right pointer to the left to decrease the sum
