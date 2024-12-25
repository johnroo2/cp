from typing import List

def productExceptSelf(self, nums: List[int]) -> List[int]:
    zeroes = nums.count(0)
    
    if zeroes == len(nums):
        return nums

    total = 1
    nonZeroTotal = 1

    for num in nums:
        if num != 0:
            total *= num
        nonZeroTotal *= num

    return list(map(lambda i: (total if zeroes < 2 else 0) if i == 0 else int(nonZeroTotal/i), nums))