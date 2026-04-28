class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minHeap with k elements (since we never remove any numbers)
        # --> A number which is not k largest number at one time, 
        # will never be a k largest number
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # Smallest is always stored at index 0
        return self.minHeap[0]
        
