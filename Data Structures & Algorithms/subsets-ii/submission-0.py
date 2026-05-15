class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        if len(nums) == 0:
            return []

        def helper(i , curr):
            if i == len(nums):
                res.append(curr[:])
                return
            
            # First choice: include
            # Find next uniques number
            curr.append(nums[i])
            helper(i + 1, curr)

            # Second choice: exclude
            curr.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(i + 1, curr)
        helper(0, [])
        return res
