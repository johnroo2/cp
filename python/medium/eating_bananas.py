import math
from typing import List

def minEatingSpeed(self, piles: List[int], h: int) -> int:
    pile_limit = 1000000000

    l, r = 1, pile_limit

    while l <= r:
        m = l + ((r - l) // 2)

        eating_time = sum(map(lambda i: math.ceil(i / m), piles))

        if eating_time <= h:
            r = m - 1
        else:
            l = m + 1
    
    return l
