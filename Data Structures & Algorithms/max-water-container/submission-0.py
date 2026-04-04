class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # moving the taller pointer guarantees a smaller or equal volume
        # since height is capped by the smaller
        left, right = 0, len(heights) - 1
        n = left - right
        vol = 0
        maxVol = self.calVol(heights[left], heights[right], left, right)
        while left < right:
            if heights[left] > heights[right]:
                right-=1
            else: 
                left += 1
            maxVol = max(maxVol, self.calVol(heights[left], heights[right], left, right))
        return maxVol


    def calVol(self, left: int, right:int, idx1: int, idx2: int) -> int:
        return (idx2 - idx1) * min(left, right)