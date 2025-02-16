from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []

        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))

        times.sort(key=lambda i: (i[0], i[1]))

        res, step = 0, 0

        for time in times:
            step += time[1]
            res = max(step, res)

        return res