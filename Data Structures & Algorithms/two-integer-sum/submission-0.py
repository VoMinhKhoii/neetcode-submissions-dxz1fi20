class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        # n is also a value at index i, no need nums[i]
        for i in range(len(nums)):
            
            diff = target - nums[i]
            if diff in dict:
                return [dict[diff], i]
            dict[nums[i]] = i 
        return []