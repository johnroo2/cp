from typing import List

def encode(self, strs: List[str]) -> str:
        sizeEncodings = ""
        for s in strs:
            sizeEncodings += str(len(s)) + "#" + s
        return sizeEncodings

def decode(self, s: str) -> List[str]:
    i = 0
    strings = []

    while i < len(s):
        j = i
        while s[j] != '#':
            j += 1
        strLength = int(s[i:j])
        i = j + 1
        j = i + strLength
        strings.append(s[i:j])
        i = j
    
    return strings