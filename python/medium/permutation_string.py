
def checkInclusion(self, s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False

    counts1, counts2 = {}, {}

    for char in s1:
        counts1[char] = 1 + counts1.get(char, 0)

    l, r = 0, 0

    while r < len(s2):
        counts2[s2[r]] = 1 + counts2.get(s2[r], 0)

        if r - l + 1 == len(s1):
            if counts1 == counts2:
                return True

            counts2[s2[l]] -= 1
            if counts2[s2[l]] == 0:
                del counts2[s2[l]]
            l += 1

        r += 1

    return False
