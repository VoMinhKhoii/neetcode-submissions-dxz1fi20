import sys
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest_pile = -sys.maxsize - 1
        min_k = sys.maxsize + 1
        for i in piles:
            if i >= largest_pile:
                largest_pile = i
        
        # UPPER BOUND
        # k = largest_pile when h = piles.length 
        left, right = 1, largest_pile

        while left <= right:
            k = (left + right) // 2
            h_with_current_k = 0
            for i in piles:
                h_with_current_k += math.ceil(i / k)

            if h_with_current_k == h:
                return k

            if h_with_current_k > h:
                left = k + 1
            if h_with_current_k < h:
                right = k - 1
                min_k = k
        return min_k
            

        