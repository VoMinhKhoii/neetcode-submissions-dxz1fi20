class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # If we try to update the frequency while iterating through nums
        # We will have to iterate through the inside array
        # -> One pass is inefficient

        # Two pass:
        # 1. Keep a frequency map of nums ({nums[i] : frequency})
        # 2. Bucket sort

        # 1
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        
        # 2
        # bucket = defaultdict(list)
        # for key, value in freq:
        #     bucket[value] = bucket.get(key, 0).append(key)
        # CRTICAL: Cant use dict as bucket since it has no orders
        # order of dict is based on the order we add in
        # ITERATE IN REVERSED ORDER WONT WORK
        # -> LIST OF LIST INSTEAD

        bucket= [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            bucket[count].append(num)

        # THIS IS WRONG, CANT SHORTCUT HERE SINCE K REPRESENTS NUMS OF ELEMENTS
        # DOING LIKE BELOW WILL SEE K AS NUMS OF BUCKET
        # Iterate backwards
        # curr = 0
        # res = []
        # for i in range(len(bucket) - 1, 0 , -1):
        #     if curr >= k:
        #         return res
        #     res += bucket[i]
        #     curr += 1
        # return res
        curr = 0
        res = []
        for i in range(len(bucket) - 1, 0 , -1):
            for n in bucket[i]:
                if curr >= k:
                    return res
                else:
                    curr += 1
                    res.append(n)
        return res


            

        