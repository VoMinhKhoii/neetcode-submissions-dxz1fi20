import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # ROTATION:
        # nums of rotation = k
        # Looking from right to left k elements, put those k element to the beginning
        # of the array.
        # Ex: [10, 20, 30, 40, 50, 60, 70] rotate 3 times -> [50,60,70,10, 20, 30, 40]

        # We want to find the first element, of the second part of the nums
        # If mid > L --> mid in first part of arrat --> Shift left
        # if mid < R --> mid in second part of array --> Shift right
        # min is the one that keeps on satisfy the second requirements

        left, right = 0, len(nums) - 1
        # min_val = sys.maxsize + 1
        mid = 0
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] <= nums[right]:
                right = mid
                continue
            if nums[mid] >= nums[left]:
                left = mid + 1
        return nums[right] | nums[left] #These are the same at the end of the day