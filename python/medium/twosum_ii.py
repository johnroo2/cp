from typing import List

def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while low < high:
            curSum = numbers[low] + numbers[high]
            if curSum > target:
                high -= 1
            elif curSum < target:
                low += 1
            else:
                return [low + 1, high + 1]
                
        return []