class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in freq.items():
            buckets[value].append(key)
        
        retVal = [item for bucket in buckets for item in bucket]
        return retVal[::-1][:k]