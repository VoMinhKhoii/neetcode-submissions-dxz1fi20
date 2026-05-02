class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We use a maxHeap: negate every value in the first array, then heappify
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)
        res = 0
        for i in range(k):
            res = -heapq.heappop(max_heap)
        return res
        