class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums)-1
        left = 0
        while left < len(nums) and left <= right:
            if nums[left] == val:
                nums[left] = nums[right]
                right -= 1
                continue
            left += 1
        return left
