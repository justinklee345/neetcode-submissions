class Solution:

    def rob(self, nums: List[int]) -> int:
        def robber(nums):
            '''
            rob[i] represents the max money robbed to the ith house
            rob[i] = max(rob[i-1], rob[i-2] + nums[i])
            rob[1] = max(rob[0], nums[1])
            rob[0] = nums[0]
            '''
            rob = []
            for i in range(len(nums)):
                if i == 0:
                    rob.append(nums[0])
                    continue

                if i == 1:
                    rob.append(max(rob[0], nums[1]))
                    continue
                
                rob.append(max(rob[i-1], rob[i-2] + nums[i]))
            return rob[-1]
        
        if len(nums) == 1:
            return nums[0]
        return max(robber(nums[1:]), robber(nums[:-1]))