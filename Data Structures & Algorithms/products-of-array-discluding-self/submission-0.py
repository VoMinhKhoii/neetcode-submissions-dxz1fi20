class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productArr = []
        leftProduct = [1]
        rightProduct = [1]

        curr = 1
        for i in nums:
            curr = curr * i
            leftProduct.append(curr)
        
        # left = [1,1,2,8,48]
        # right = [1,6,24,48,48]
        curr = 1
        for i in nums[::-1]:
            curr = curr * i
            rightProduct.append(curr)
        rightProduct.append(1)

        n = len(nums)
        for i in range(n):
            res = leftProduct[i] * rightProduct[n-(i+1)]
            productArr.append(res)
        return productArr

            
        