class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for i in range(len(nums)):
            if dict.get(nums[i], 0) > 0:
                return True
            dict[nums[i]] = 1
        return False
        