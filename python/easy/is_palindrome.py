def isPalindrome(self, s: str) -> bool:
    stripped = ''.join(ch for ch in s if ch.isalnum()).lower()
    low = 0
    high = len(stripped) - 1

    while low < high:
        if stripped[low] != stripped[high]:
            return False
        low += 1
        high -= 1
    
    return True