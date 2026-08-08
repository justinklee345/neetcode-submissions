"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # this is just two different doors that we keep track of separately

        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        print(starts)
        print(ends)
        s, e = 0, 0
        cnt, maxcnt = 0, float("-inf")
        while s < len(starts):
            if ends[e] <= starts[s]:
                cnt -= 1
                e += 1
            else:
                cnt += 1
                s += 1
            maxcnt = max(maxcnt, cnt)
            
        return maxcnt if maxcnt != float("-inf") else 0