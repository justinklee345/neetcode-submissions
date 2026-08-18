class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxPrice = 0
        for r in range(len(prices)):
            maxPrice = max(maxPrice, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
        return maxPrice
            