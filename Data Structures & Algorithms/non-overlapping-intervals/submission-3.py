class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]
        cnt = 0
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev[1] > curr[0]:
                if curr[1] < prev[1]:
                    prev = curr
                cnt += 1
            else:
                prev = curr

        return cnt



