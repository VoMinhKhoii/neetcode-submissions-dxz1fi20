class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Since heapq is min heap by default
        # So we can work with negated value, then negate it back before process
        max_heap = []
        for i in stones:
            max_heap.append(-i)
        heapq.heapify(max_heap)
        while len(max_heap) > 1:
            heaviest = -heapq.heappop(max_heap)
            second_heaviest = -heapq.heappop(max_heap)
            if heaviest == second_heaviest:
                continue
            else:
                heapq.heappush(max_heap, -(heaviest - second_heaviest))
        if len(max_heap) == 1:
            return -max_heap[0]
        else: return 0
        
