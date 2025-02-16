from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        i = 0
        res = []

        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
            i += 1
        
        l, r = newInterval[0], newInterval[1]

        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            l = min(l, intervals[i][0])
            r = max(r, intervals[i][1])
            i += 1

        res.append([l, r])

        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res
            
            