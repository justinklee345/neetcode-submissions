class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        s_nums = sorted(nums)
        

        retList = set()
        for k in range(len(nums)):
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if s_nums[i] + s_nums[j] + s_nums[k] == 0:
                    retList.add((s_nums[i], s_nums[j], s_nums[k]))
                    i += 1
                    j -= 1
                elif s_nums[i] + s_nums[j] + s_nums[k] > 0:
                    j -= 1
                else:
                    i += 1
                    
        return [list(i) for i in list(retList)]
        