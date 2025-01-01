import heapq
from typing import List

def findKthLargest(self, nums: List[int], k: int) -> int:
    nums = [-n for n in nums]
    heapq.heapify(nums)

    for _ in range(k - 1):
        heapq.heappop(nums)
    
    return -heapq.heappop(nums)
