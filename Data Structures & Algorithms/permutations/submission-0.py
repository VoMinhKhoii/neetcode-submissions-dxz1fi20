class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        def helper(curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    # We want to skip whats already used
                    curr.append(nums[i])
                    used[i] = True

                    helper(curr)

                    # Since its popped, its not used
                    curr.pop()
                    used[i] = False
        helper([])
        return res
