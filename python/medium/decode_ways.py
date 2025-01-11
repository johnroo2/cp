class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1

        for i in range(2, len(s) + 1):
            single, double = int(s[i - 1 : i]), int(s[i - 2 : i])

            if 1 <= single <= 9:
                dp[i] += dp[i - 1]
            
            if 10 <= double <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]
