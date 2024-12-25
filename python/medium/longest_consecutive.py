from typing import List

def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for num in numSet:
        if not num - 1 in numSet:
            l = 0
            while (num + l) in numSet:
                l += 1
            if l > longest:
                longest = l
    
    return longest