class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        reverse = [1 for i in range(len(nums))]
        forward = [1 for i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            reverse[i] = nums[i + 1] * reverse[i + 1]
        for i in range(1, len(nums)):
            forward[i] = nums[i - 1] * forward[i - 1]
        
        print(reverse)
        print(forward)
        retList = []

        for i in range(len(nums)):
            retList.append(reverse[i] * forward[i])

        return retList

