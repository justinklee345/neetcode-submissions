class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        before, overlap, after = [], [newInterval], []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                before.append(interval)
                continue
            
            if newInterval[1] < interval[0]:
                after.append(interval)
                continue
            
            overlap.append(interval)

        return before + [[min([ele[0] for ele in overlap]), max([ele[1] for ele in overlap])]] + after
        