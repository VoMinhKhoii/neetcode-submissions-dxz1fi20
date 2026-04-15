import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # AIM: Find the cut point, aka min val
        left, right = 0, len(nums) - 1
        mid = 0
        while left <= right:
            mid = int((left + right) / 2)
            if target == nums[mid]:
                return mid

            # Identify which half mid is in:
            if nums[mid] > target:
                if target > nums[left]:
                    right = mid - 1
                else: 
                    left = mid + 1
            if nums[mid] < target:
                if target > nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1