class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vocab = {}

        for i, num in enumerate(nums):
            if target - num in vocab.keys():
                return [vocab[target - num] , i]
            vocab[num] = i
        