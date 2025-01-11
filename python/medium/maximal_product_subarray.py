from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cmin, cmax = 1, 1

        for num in nums:
            tmp = cmax * num
            cmax = max(num * cmin, num * cmax, num)
            cmin = min(tmp, num * cmin, num)
            res = max(cmax, res)

        return res
        