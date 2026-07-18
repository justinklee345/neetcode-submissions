import math, heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = [(math.sqrt(point[0] ** 2 + point[1] ** 2), point) for point in points]
        heapq.heapify(maxHeap)
        retList = []
        for _ in range(k):
            point = heapq.heappop(maxHeap)[1]
            retList.append(point)
        return retList