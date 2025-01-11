import heapq
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 2:
            return 0 if not cost else cost[0]

        vals = [float("inf")] * len(cost)
        heap = [(0, -1)] 

        while heap:
            c, pos = heapq.heappop(heap)
            if 0 <= pos < len(cost):
                vals[pos] = min(vals[pos], c)
            
            if pos + 1 < len(cost):
                heapq.heappush(heap, (c + cost[pos + 1], pos + 1))

            if pos + 2 < len(cost):
                heapq.heappush(heap, (c + cost[pos + 2], pos + 2))

        return min(vals[-1], vals[-2])
