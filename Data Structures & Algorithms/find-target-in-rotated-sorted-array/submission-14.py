class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else: 
                return -1
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2
            left, mid, right = nums[l], nums[m], nums[r]

            if target == mid:
                return m
            if target == left:
                return l
            if target == right:
                return r

            if left <= mid <= right:
                if target > mid:
                    l = m + 1
                else:
                    r = m - 1
            
            if left >= mid <= right:
                if mid < target < right:
                    l = m + 1
                else:
                    r = m - 1

            
            if left <= mid >= right:
                if left < target < mid:
                    r = m - 1
                else:
                    l = m + 1

            if left >= mid >= right:
                if target > mid:
                    r = m - 1
                else:
                    l = m + 1
        return -1

