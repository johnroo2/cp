from typing import List

def maxArea(self, heights: List[int]) -> int:
    l, r = 0, len(heights) - 1
    maxArea = 0

    while l < r:
        area = min(heights[l], heights[r]) * (r - l)
        maxArea = max(maxArea, area)

        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    
    return maxArea