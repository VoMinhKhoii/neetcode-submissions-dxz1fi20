class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def helper(i , remaining , curr):
            if remaining == 0:
                res.append(curr[:])
                return
            if i >= len(nums) or remaining < 0:
                return
            
            # First choice: include
            curr.append(nums[i])
            helper(i, remaining - nums[i], curr)

            # Second choice: exclude
            curr.pop()
            helper(i+1, remaining, curr)
            

        helper(0, target, [])
        return res

