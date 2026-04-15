import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # BEING ABLE TO KNOW WHEN TO SHIFT LEFT/RIGHT
        # We must know which side is sorted
        left, right = 0, len(nums) - 1
        mid = 0
        while left <= right:
            mid = int((left + right) / 2)
            if target == nums[mid]:
                return mid

            # Identify which side is sorted
            if nums[left] <= nums[mid]:
                # Left side is sorted
                if nums[left] < target < nums[mid]:
                    right = mid -1
                else: 
                    left = mid + 1
            else:
                # right side is sorted
                if nums[mid] < target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1