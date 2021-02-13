class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if i == -1 or j == -1:
                return 0
            if text1[i] == text2[j]:
                memo[(i, j)] = dp(i-1, j-1) + 1
            else:
                memo[(i, j)] = max(
                    dp(i-1, j),
                    dp(i, j-1)
                )
            return memo[(i, j)]
        return dp(len(text1)-1, len(text2)-1)

    def longestCommonSubsequence_2(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:  # just be careful of index (of sth: no its danger and try to avoid it; with sth: treat it gently and respectfully)
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

test = Solution()
text1 = "abc"
text2 = "def"
res = test.longestCommonSubsequence(text1, text2)
res = test.longestCommonSubsequence_2(text1, text2)
print(res)