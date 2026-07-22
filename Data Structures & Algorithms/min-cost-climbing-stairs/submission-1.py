class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # minCost[i] represents the min cost needed to get to i floor
        # minCost[i] = min(minCost[i-1] + cost[i-1], minCost[i-2] + cost[i-2])
        # base cases: minCost[0] = 0, minCost[1] = 0

        prev1, prev2 = 0, 0

        for i in range(2, len(cost) + 1):
            curr = min(prev1 + cost[i-2], prev2 + cost[i-1])
            prev1 = prev2
            prev2 = curr

        return prev2