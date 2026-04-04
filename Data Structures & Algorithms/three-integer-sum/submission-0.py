class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for idx in range(len(nums) - 3):
            left, right = idx + 1 , len(nums) - 1
            target = 0 - nums[idx]
            while nums[left] + nums[right] != target and left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
            if left >= right:
                continue
            if nums[left] + nums[right] == target:
                triplets = [nums[idx], nums[left], nums[right]]
                res.append(triplets)
        return res