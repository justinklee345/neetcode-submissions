class Wrapper:
    def __init__(self, num, cnt):
        self.num = num
        self.cnt = cnt

    def __lt__(self, other):
        return self.cnt < other.cnt

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        heap = []
        for key, value in counter.items():
            heapq.heappush(heap, Wrapper(key, -1 * value))

        res = []
        for i in range(k):
            popped = heapq.heappop(heap)
            res.append(popped.num)
        
        return res