class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # maxRob[i] represents the maximum amount you can rob from house 0 to house i
        # maxRob[i] = max(maxRob[i-2] + nums[i], maxRob[i-1])
        # base cases: maxRob[0] = cost[0], maxRob[1] = cost[1]

        maxRob = []

        for i in range(0, len(nums)):
            if i == 0:
                maxRob.append(nums[i])
                continue
            
            if i == 1:
                maxRob.append(max(nums[i], maxRob[i-1]))
                continue
            
            maxRob.append(max(maxRob[i-2] + nums[i], maxRob[i-1]))

        print(maxRob)
        return maxRob[-1]

"""
1 1 
4 1 1 5

"""

