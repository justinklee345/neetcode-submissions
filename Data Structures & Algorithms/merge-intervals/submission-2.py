class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []: return []

        intervals = sorted(intervals, key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            prev = res[-1]

            if prev[1] < curr[0]:
                res.append(curr)
                continue
            
            res.pop()
            res.append([min(prev[0], curr[0]), max(prev[1], curr[1])])
        return res
