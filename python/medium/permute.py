from typing import List

class Solution:
    def helper(self, nums: List[int], index: int) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        res = []
        cnums = nums.copy()
        if index >= 0:
            del cnums[index]

        prefix = [nums[index]] if index >= 0 else []

        for i in range(len(cnums)):
            subperms = list(map(lambda l: prefix + l, self.helper(cnums, i)))
            res.extend(subperms)

        return res

    
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, -1)