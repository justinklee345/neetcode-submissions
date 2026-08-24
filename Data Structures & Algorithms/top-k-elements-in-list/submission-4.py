class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]
        freq_map = {}

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num, freq in freq_map.items():
            freqs[freq].append(num)
        
        traverse = freqs[::-1]
        cnt = 0
        res = []
        for freq in traverse:
            if not freq:
                continue
            for ele in freq:
                res.append(ele)
                cnt += 1
                if cnt == k:
                    break
            if cnt == k:
                break
        return res


