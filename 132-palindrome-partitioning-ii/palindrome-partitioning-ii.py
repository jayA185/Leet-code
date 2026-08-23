class Solution:
    def minCut(self, s):
        n = len(s)

        # dp[i] = minimum cuts needed for s[0:i+1]
        dp = list(range(n))

        # palindrome[i][j] = True if s[i:j+1] is palindrome
        palindrome = [[False] * n for _ in range(n)]

        for end in range(n):
            for start in range(end + 1):

                if s[start] == s[end] and (
                    end - start <= 2 or palindrome[start + 1][end - 1]
                ):
                    palindrome[start][end] = True

                    if start == 0:
                        dp[end] = 0
                    else:
                        dp[end] = min(
                            dp[end],
                            dp[start - 1] + 1
                        )

        return dp[n - 1]