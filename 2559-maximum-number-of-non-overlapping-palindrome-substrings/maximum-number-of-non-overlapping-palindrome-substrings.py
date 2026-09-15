class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pal = [bytearray(n) for _ in range(n)]
        for i in range(n):
            pal[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and (length == 2 or pal[i + 1][j - 1]):
                    pal[i][j] = 1
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1]
            for j in range(i):
                if i - j >= k and pal[j][i - 1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return dp[n]