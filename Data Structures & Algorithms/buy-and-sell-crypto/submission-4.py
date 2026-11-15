class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minVal = float('inf')
        maxProfit = 0
        for price in prices:
            maxProfit = max(maxProfit, price - minVal)
            minVal = min(minVal, price)
        return maxProfit
