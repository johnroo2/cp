from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, t in times:
            adj[u].append((v, t))

        heap = [(0, k)]
        visit = set()
        time = 0

        while heap:
            t, node = heapq.heappop(heap)
            if node in visit:
                continue
            visit.add(node)
            time = max(time, t)

            for nei, d in adj[node]:
                if nei not in visit:
                    heapq.heappush(heap, (t + d, nei))

        return time if len(visit) == n else -1
