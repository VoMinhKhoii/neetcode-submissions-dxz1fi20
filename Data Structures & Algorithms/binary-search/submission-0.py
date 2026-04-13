class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums) - 1
        while left <= right:
            mid = int((left + right) / 2)
            if target == nums[mid]:
                return mid
            # if just left or right = mid, there will be an indefinite loop
            # for ex, an array with only 2 elements.
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid -1
        return -1
        