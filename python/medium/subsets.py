from typing import List

def subsets(self, nums: List[int]) -> List[List[int]]:
    res = [[]]

    c = 1

    for i in range(len(nums)):
        for j in range(c):
            res.append(res[j] + [nums[i]])
        
        c *= 2

    return res