def lengthOfLongestSubstring(self, s: str) -> int:
    chars = set()
    longest = 0
    l, r = 0, 0

    while r < len(s):
        if s[r] in chars:
            while s[l] != s[r]:
                chars.discard(s[l])
                l += 1
            chars.discard(s[l])
            l += 1
        chars.add(s[r])
        longest = max(longest, len(chars))
        r += 1
        
    return longest