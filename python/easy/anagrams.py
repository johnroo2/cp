def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = [0 for i in range(26)]

    for i in range(0, len(s)):
        counts[ord(s[i]) - ord('a')] += 1
        counts[ord(t[i]) - ord('a')] -= 1
    
    for key in counts:
        if key != 0: 
            return False

    return True