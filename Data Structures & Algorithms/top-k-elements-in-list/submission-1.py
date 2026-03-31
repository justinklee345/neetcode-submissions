class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topMap = {}

        for num in nums:
            if num in topMap.keys():
                topMap[num] += 1
            else:
                topMap[num] = 1

        sortedMap = sorted(topMap, key=topMap.get, reverse=True)
        return sortedMap[:k]
