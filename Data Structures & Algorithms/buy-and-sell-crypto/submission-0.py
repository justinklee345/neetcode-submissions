class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        maxProfit = 0

        while r < len(prices):
            if l == r:
                r += 1
                continue

            if prices[l] > prices[r]:
                l = r
                r += 1
                continue
            
            maxProfit = max(maxProfit, prices[r]-prices[l])
            r+= 1
        
        return maxProfit
