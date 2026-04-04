class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx in range(len(nums) - 2):
            left, right = idx + 1 , len(nums) - 1
            target = 0 - nums[idx]
            while left < right:
                if nums[left] + nums[right] == target:
                    triplets = [nums[idx], nums[left], nums[right]]
                    res.append(triplets)
                    left+=1
                if nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
                if left >= right:
                    continue

        res = [list(t) for t in set(tuple(i) for i in res)]
        return res