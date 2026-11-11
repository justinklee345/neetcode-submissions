class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        find = {}

        for idx, i in enumerate(nums):
            if target - i in find:
                return [find[target-i], idx]
            else:
                find[i] = idx
        
        