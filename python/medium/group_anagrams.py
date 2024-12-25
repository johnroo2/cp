from typing import List
from collections import defaultdict

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    def encode(s):
        counts = [0 for _ in range(26)]
        for i in range(len(s)):
            counts[ord(s[i]) - ord('a')] += 1
        return tuple(counts)
    
    groups = defaultdict(list)
    
    for str in strs:
        groups[encode(str)].append(str)
        
    return list(groups.values())
    
                    
