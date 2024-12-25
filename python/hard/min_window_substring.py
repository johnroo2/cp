def minWindow(self, s: str, t: str) -> str:
    minstring = None

    counts1, counts2 = {}, {}

    for i in range(len(t)):
        counts1[t[i]] = 1 + counts1.get(t[i], 0)
    
    l, r = 0, 0

    while r < len(s):
        counts2[s[r]] = 1 + counts2.get(s[r], 0)

        if r - l + 1 >= len(t):
            broken = False
            for key in counts1:
                if key not in counts2 or counts1[key] > counts2[key]:
                    broken = True
            if not broken:
                if not minstring or len(s[l:r+1]) <= len(minstring):
                    minstring = s[l:r+1]

                while l <= r:
                    counts2[s[l]] = -1 + counts2.get(s[l], 0)
                    if counts2[s[l]] == 0:
                        del counts2[s[l]]

                    l += 1

                    broken = False
                    for key in counts1:
                        if key not in counts2 or counts1[key] > counts2[key]:
                            broken = True 
                    if not broken:
                        if not minstring or len(s[l:r+1]) <= len(minstring):
                            minstring = s[l:r+1]
                    else:
                        break
        r += 1

    return minstring if minstring else ""

#gpt solution
def minWindow(self, s: str, t: str) -> str:
    if not t or not s:
        return ""

    counts1 = {}
    for char in t:
        counts1[char] = 1 + counts1.get(char, 0)

    counts2 = {}
    required = len(counts1)
    formed = 0

    l, r = 0, 0
    min_len = float('inf')
    min_window = (0, 0)

    while r < len(s):
        char = s[r]
        counts2[char] = 1 + counts2.get(char, 0)

        if char in counts1 and counts2[char] == counts1[char]:
            formed += 1

        while l <= r and formed == required:
            if r - l + 1 < min_len:
                min_len = r - l + 1
                min_window = (l, r)

            left_char = s[l]
            counts2[left_char] -= 1
            if left_char in counts1 and counts2[left_char] < counts1[left_char]:
                formed -= 1

            l += 1

        r += 1

    l, r = min_window
    return s[l:r+1] if min_len != float('inf') else ""