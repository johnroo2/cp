from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda i: i.start)

        l, r = intervals[0].start, intervals[0].end

        for i in range(1, len(intervals)):
            if intervals[i].start < r and intervals[i].end > l:
                return False
            l = min(l, intervals[i].start)
            r = max(r, intervals[i].end)

        return True
