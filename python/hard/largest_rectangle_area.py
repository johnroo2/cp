from typing import List

def largestRectangleArea(self, heights: List[int]) -> int:
    maxArea = 0
    stack = []

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, pos = stack.pop()
            maxArea = max(maxArea, pos * (i - index))
            start = index
        stack.append((start, h))
    
    for rem in stack:
        maxArea = max(maxArea, rem[1] * (len(heights) - rem[0]))
    
    return maxArea