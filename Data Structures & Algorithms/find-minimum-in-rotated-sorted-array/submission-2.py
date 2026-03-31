class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        print(nums)

        while l <= r:
            print(l, r)
            m = l + ((r-l) // 2)

            if nums[l] < nums[m] < nums[r]:
                r = m
            elif nums[l] < nums[m]:
                l = m
            elif nums[m] < nums[r]:
                r = m
            else:
                break

        print(l, r, "bruh")
        return nums[r]

# 3 4 5 6 1 2 (3, 5, 2)
# 6 1 2 (6, 1, 2)
# 6 1 (6, 6, 1)





# 4 5 6 1 2 3 (4, 6, 3)
# 123 (1 2 3)


# 5 6 1 2 3 4 (5, 1, 4)
# 5 6 1

# 6 1 2 3 4 5 (6, 2, 5)
# 1 2 3 4 5 6 (1, 3, 6)
# 2 3 4 5 6 1 (2, 4, 1)


        