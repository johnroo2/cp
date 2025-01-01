from typing import List

class Solution:
    def helper(self, nums: List[int], target: int, index: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        if target < 0 or index == len(nums):
            return []
        
        res = []
        include = self.helper(nums, target - nums[index], index)
        for l in include:
            res.append([nums[index]] + l)

        exclude = self.helper(nums, target, index + 1)
        res.extend(exclude)

        return res


    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        return self.helper(nums, target, 0)
        