class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vocab = set()

        for num in nums:
            if num in vocab:
                return True
            vocab.add(num)
        return False