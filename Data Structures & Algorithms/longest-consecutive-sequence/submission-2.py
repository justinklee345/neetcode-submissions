class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            seen.add(num)
        
        cnt = 0
        for i, num in enumerate(nums):
            if num - 1 in seen:
                continue
            
            idx = 0
            while idx < len(nums) and num + idx in seen:
                cnt = max(cnt, idx + 1)
                idx += 1
        return cnt