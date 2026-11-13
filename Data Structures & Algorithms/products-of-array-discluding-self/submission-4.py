class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totheleft = [1 for _ in range(len(nums))]
        totheright = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            totheleft[i] = totheleft[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            totheright[i] = totheright[i + 1] * nums[i + 1]
        
        res = []
        for i in range(len(nums)):
            res.append(totheleft[i] * totheright[i])
        return res