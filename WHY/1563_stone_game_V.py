from typing import List

class Solution:
    """
    Ref: https://leetcode.com/problems/stone-game-v/discuss/807330/C++-O(N2)-DP
        I am still confused...
    """
    def stoneGameV(self, stones: List[int]):
        n = len(stones)
        A = [0]
        for x in stones:
            A.append(A[-1] + x)
            
        dp = [[0] * (n+1) for _ in range(n+1)]
        f, g = [0] * (n+1), [0] * (n+1)
        x, y = [0] * (n+1), [0] * (n+1)
        
        for i in range(1,n+1):
            x[i], y[i] = i, i - 1
        
        for l in range(2, n + 1):
            for i in range(1, n+1):
                j = i + l - 1
                if j > n:
                    break

                half = (A[j] - A[i-1]) // 2
                
                while x[i] < j and A[x[i]] - A[i-1] <= half:
                    f[i] = max(f[i], A[x[i]] - A[i-1] + dp[i][x[i]])
                    x[i] += 1
                    
                while y[j] >= i and A[j] - A[y[j]] <= half:
                    g[j] = max(g[j], A[j] - A[y[j]] + dp[y[j]+1][j])
                    y[j] -= 1
                    
                dp[i][j] = max(f[i], g[j])

        return dp[1][n]