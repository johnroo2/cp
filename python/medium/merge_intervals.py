from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        res = []
        intervals.sort(key=lambda i: i[0])

        i = 0

        while i < len(intervals):
            l, r = intervals[i][0], intervals[i][1]
            i += 1

            while i < len(intervals) and ((intervals[i][0] >= l and intervals[i][0] <= r) or
                (intervals[i][1] >= l and intervals[i][1] <= r)):
                l = min(l, intervals[i][0])
                r = max(r, intervals[i][1])
                i += 1

            res.append([l, r])

        return res
                


        