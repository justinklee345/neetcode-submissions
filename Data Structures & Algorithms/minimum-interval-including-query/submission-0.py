class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # brute
        
        intervals.sort(key=lambda x: x[0])
        res = []
        for query in queries:
            smallest = float('inf')

            for interval in intervals:
                if interval[0] <= query <= interval[1]:
                    smallest = min(smallest, interval[1] - interval[0] + 1)
            
            if smallest == float("inf"):
                res.append(-1)
                continue
            res.append(smallest)
        return res