class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLen = 0
        numSet = set(nums)

        for num in numSet:
            if num - 1 not in numSet: # O(1) lookup
                length = 0

                while num + length in numSet:
                    length += 1
                
                maxLen = max(length, maxLen)

        return maxLen