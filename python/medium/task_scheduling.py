from typing import List

def leastInterval(self, tasks: List[str], n: int) -> int:
    counts = [0] * 26

    for task in tasks:
        counts[ord(task) - ord("A")] += 1

    counts.sort(reverse = True)

    highest_frequency, i = counts[0], 0

    while counts[i] == highest_frequency:
        i += 1
    
    return max(len(tasks), (n + 1) * (counts[0] - 1) + i)
