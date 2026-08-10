class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currMin, currMax = 1, 1
        for num in nums:
            tmp = currMax
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(tmp * num, currMin * num, num)
            res = max(res, currMax)
        return res

        