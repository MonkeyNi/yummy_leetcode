class Solution:
    def rearrangeSticks(self, n: int, k: int):
        # dp[i][j]: we have i sticks and j left visible
        # when we add a smallest stick to the array, there are two situsations
        # 1. add to the left: which mean now we have (j+1) visible
        # 2. do not add to the left: then j will not be affected and there are i different
        #    methods;
        # so, dp[i+1][j] = dp[i][j]*i + dp[i][j-1]
        # dp[i][j] = dp[i-1][j]*(i-1) + dp[i-1][j-1]

        # It does not matter whether we choose biggest stick (add to right) or smallest (add to left).
        
        dp = [[0]*(k+1) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(1, min(n, k)+1):
                dp[i][j] = dp[i-1][j]*(i-1) + dp[i-1][j-1]
                dp[i][j] %= (10**9+7)
        return int(dp[n][k]%(10**9+7))
                