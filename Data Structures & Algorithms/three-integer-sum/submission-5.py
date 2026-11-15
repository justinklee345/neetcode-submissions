class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        res = []

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    print(i, l, r)
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
                elif curr < 0:
                    l += 1
                else:
                    r -= 1
        
        return res

"""

[-1,0,1,2,-1,-4]
[-4, -1, -1, 0, 1, 2]

"""