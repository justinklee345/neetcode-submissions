class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for key, value in freq.items():
            buckets[value].append(key)
        
        cnt = 0
        retVal = []
        for bucket in buckets[::-1]:
            if len(bucket) != 0:
                cnt += len(bucket)
                
                for item in bucket:
                    retVal.append(item)
            if cnt == k:
                return retVal
        