class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(i, nums, curr):
            if i == len(nums):
                res.append(curr[:])
                return
            helper(i+1, nums, curr)
            curr.append(nums[i])
            helper(i+1, nums, curr)
            curr.pop()
        helper(0, nums, [])
        return res