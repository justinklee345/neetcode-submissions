import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [stone * -1 for stone in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x == y:
                continue
            
            heapq.heappush(maxHeap, -1 * abs(x - y))
        
        if maxHeap:
            return -1 * maxHeap[0]
        return 0