from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        memo = {}

        def helper(start, i):
            if (start, i) in memo:
                return memo[(start, i)]
            elif i <= 2:
                memo[(start, i)] = max(nums[start:start+i])
            else:
                memo[(start, i)] = max(helper(start, i - 1), helper(start, i - 2) + nums[start + i - 1])
            return memo[(start, i)]

        return max(helper(0, len(nums) - 1), helper(1, len(nums) - 1))

        