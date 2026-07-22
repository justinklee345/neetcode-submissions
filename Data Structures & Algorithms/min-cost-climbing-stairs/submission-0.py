class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # minCost[i] represents the min cost needed to get to i floor
        # minCost[i] = min(minCost[i-1] + cost[i-1], minCost[i-2] + cost[i-2])
        # base cases: minCost[0] = 0, minCost[1] = 0

        minCost = []

        for i in range(len(cost) + 1):
            if i <= 1:
                minCost.append(0)
                continue
            
            minCost.append(min(minCost[i-1] + cost[i-1], minCost[i-2] + cost[i-2]))

        return minCost[-1]