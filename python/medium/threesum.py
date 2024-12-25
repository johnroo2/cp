from typing import List

def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = set()

    for i in range(len(nums)):
        target = -nums[i]
        sumset = set()
        
        for j in range(i, len(nums)):
            if j == i: 
                continue
            if target - nums[j] in sumset:
                res.add(tuple(sorted([-target, nums[j], target - nums[j]])))
                sumset.remove(target - nums[j])
            else:
                sumset.add(nums[j])

    return list(map(lambda t: list(t), res))
