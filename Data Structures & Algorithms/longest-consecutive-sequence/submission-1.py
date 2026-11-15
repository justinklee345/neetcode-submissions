class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        res = 0
        for num in nums:
            if num - 1 in nums:
                continue
            
            cnt = 1
            while True:
                if num + cnt not in nums:
                    break
                cnt += 1

            
            res = max(res, cnt)
        return res

            