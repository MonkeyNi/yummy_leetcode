class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        
        # 思考如何才能得到dp[i][j], 
        # [[i, j-1], [i, j]]
        # [[i+1, j-1], [i+1, j]]
        # 需要斜着遍历或者反向遍历
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j], dp[i][j-1], dp[i+1][j])
        return dp[0][n-1]


test = Solution()
s = "bbbab"
res = test.longestPalindromeSubseq(s)
print(res)