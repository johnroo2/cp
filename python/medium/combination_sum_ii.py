from typing import List

class Solution:
    def helper(self, candidates: List[int], target: int, index: int) -> List[List[int]]:
        if target == 0:
            return [[]]
        elif target < 0 or index >= len(candidates):
            return []
        
        res = []
        
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue

            sub_combinations = self.helper(candidates, target - candidates[i], i + 1)
            for sub_comb in sub_combinations:
                res.append([candidates[i]] + sub_comb)

        return res
            

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        return self.helper(candidates, target, 0)
    