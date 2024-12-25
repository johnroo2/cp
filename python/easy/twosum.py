from typing import List

def twoSum(self, nums: List[int], target: int):
    sumset = {}
    for i in range(0, len(nums)):
        if target - nums[i] in sumset:
            return [sumset[target - nums[i]], i]
        sumset[nums[i]] = i
    
            
            
            