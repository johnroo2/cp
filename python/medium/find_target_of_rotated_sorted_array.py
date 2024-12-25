from typing import List

def search(self, nums: List[int], target: int) -> int:
    pivot = nums[0]
    l, r = 0, len(nums) - 1

    if target == pivot:
        return 0
    
    onLeft = target > pivot    

    while l <= r:
        m = l + ((r - l) // 2)
        if nums[m] == target:
            return m
        elif nums[m] >= pivot:
            #on left side
            if not onLeft:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        else:
            #on right side
            if onLeft:
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
            
    return -1