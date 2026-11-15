class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            print(l, m, r)

            if nums[l] <= nums[m] and nums[m] <= nums[r]:
                return nums[l]
            
            if nums[l] > nums[m]:
                r = m
            else:
                l = m + 1
        return nums[l]



        