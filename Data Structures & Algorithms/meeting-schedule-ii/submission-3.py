"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        s, e = 0, 0
        total = len(starts)
        cnt, maxcnt = 0, 0
        while e < total:
            if s >= total and e < total:
                break

            if starts[s] < ends[e]:
                cnt += 1
                maxcnt = max(maxcnt, cnt)
                s += 1
            elif starts[s] > ends[e]:
                cnt -= 1
                e += 1
            else:
                e += 1
                s += 1
            
        return maxcnt

