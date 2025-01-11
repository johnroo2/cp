class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def count_palindromes(left, right):
            nonlocal count
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        for center in range(n):
            count_palindromes(center, center)      # Odd-length palindromes
            count_palindromes(center, center + 1)  # Even-length palindromes

        return count
