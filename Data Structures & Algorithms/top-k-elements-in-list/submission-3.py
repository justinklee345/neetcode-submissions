class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]

        for num, cnt in counter.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            for ele in freq[i]:
                res.append(ele)
                if len(res) >= k:
                    break
            if len(res) >= k:
                break
        
        return res