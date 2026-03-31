class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = set()

        for ele in nums:
            checker.add(ele)

        if len(checker) != len(nums):
            return True

        return False