class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def helper(i , remaining , curr):
            if remaining == 0:
                res.append(curr[:])
                return
            if i >= len(candidates) or remaining < 0:
                return
            
            # First choice: include
            # Find next uniques number
            curr.append(candidates[i])
            helper(i + 1, remaining - candidates[i], curr)

            # Second choice: exclude
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            helper(i+1, remaining, curr)

        helper(0, target, [])
        return res