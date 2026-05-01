class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # We use minheap since we one k closest points to the origin
        distance_arr = []
        # We can heapify an array of tuples
        # Python heapify using the first element
        for i in points:
            distance_arr.append((i[0]**2 + i[1]**2, i))
        heapq.heapify(distance_arr)
        res = []
        for i in range(k):
            closest = heapq.heappop(distance_arr)
            res.append(closest[1])
        return res