class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currMax = 0

        for num in nums:
            currMax = max(currMax + num, num)
            res = max(currMax, res)
        return res