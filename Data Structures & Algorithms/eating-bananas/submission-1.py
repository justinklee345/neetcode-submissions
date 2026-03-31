import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)

        l = 1
        r = upper_bound + 1

        while l <= r:
            mid = l + ((r-l) // 2)
            hours = 0
            for j in range(len(piles)):
                hours += math.ceil(piles[j] / mid)

            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
        
        return l

