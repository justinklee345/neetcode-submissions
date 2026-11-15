class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxp = 0

        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                maxp = max(maxp, prices[r] - prices[l])
        return maxp
        
