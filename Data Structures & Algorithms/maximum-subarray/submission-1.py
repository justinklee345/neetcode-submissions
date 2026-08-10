class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = max(nums)
        currMax = 0

        for num in nums:
            currMax = max(currMax + num, num)
            res = max(currMax, res)
        return res