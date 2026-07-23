class Solution:
    def robi(self, nums: List[int]) -> int:
        maxRob = []

        for i in range(len(nums)):
            if i == 0: 
                maxRob.append(nums[i])
                continue
            if i == 1:
                maxRob.append(max(nums[i], maxRob[i-1]))
                continue
            
            maxRob.append(max(maxRob[i-2] + nums[i], maxRob[i-1]))
        
        return maxRob[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robi(nums[1:]), self.robi(nums[:-1]))
        # maxRob[i] represents the 