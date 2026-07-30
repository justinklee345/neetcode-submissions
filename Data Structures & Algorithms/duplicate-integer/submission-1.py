class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        for i in nums:
            cache.add(i)
        
        print(cache)
        if len(cache) != len(nums):
            return True
        return False