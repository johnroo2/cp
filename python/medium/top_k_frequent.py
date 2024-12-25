from typing import List
from collections import defaultdict

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    frequencyTable = defaultdict(lambda: [0, 0])

    for num in nums:
        frequencyTable[num][0] = num
        frequencyTable[num][1] += 1

    ktuples = sorted(list(frequencyTable.values()), key=lambda t: -t[1])[:k]
    return list(map(lambda x: x[0], ktuples))
