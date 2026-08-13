class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1]
        for i in range(1, len(nums)):
            maxlis = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    maxlis = max(LIS[j] + 1 , maxlis)
            LIS.append(maxlis)
        return max(LIS)


'''

9 1 4 2 3 3 7

(1, 0)
(1, 1)
(2, 2)
(2, 2)


LIS[i] (length, last)
'''