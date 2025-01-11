from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def helper(nums, i):
            if i in memo:
                return memo[i]
            elif i <= 2:
                memo[i] = max(nums[:i])
            else:
                memo[i] = max(helper(nums, i - 1), helper(nums, i - 2) + nums[i - 1])
            return memo[i]

        return helper(nums, len(nums))

        