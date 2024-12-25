from typing import List

def maxProfit(self, prices: List[int]) -> int:
    diff = 0
    l, r = 0, 0

    while r < len(prices):
        if prices[l] < prices[r]:
            diff = max(diff, prices[r] - prices[l])
        else:
            l = r
        r += 1
    
    return diff