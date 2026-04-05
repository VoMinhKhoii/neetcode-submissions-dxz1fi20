class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,sell = 0,1
        maxProfit = 0
        for idx, val in enumerate(prices):
            if sell == len(prices):
                break
            maxProfit = max(prices[sell] - prices[buy], maxProfit)
            if val < prices[buy]:
                buy = idx
            if val > prices[sell]:
                sell = idx
            sell += 1
        return maxProfit

