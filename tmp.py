from typing import List

class Solution:
    # Time complexity: O(n^3)
    #   still not the best, reduce it to O(n^2)
    def stoneGameV(self, stoneValue: List[int]):
        if len(stoneValue) <= 1:
            return 0

        n = len(stoneValue)
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + stoneValue[i]
        dp_table = [[0 for _ in range(n+1)] for _ in range(n+1)]

        def dp(i, j):
            if i == j:
                return 0
            if dp_table[i][j] != 0:
                return dp_table[i][j]
            res = 0
            for m in range(i, j):
                left = prefix[m+1] - prefix[i]
                right = prefix[j+1] - prefix[m+1]
                if left <= right:
                    res = max(res, dp(i, m) + left)
                # ???
                if left >= right:
                    res = max(res, dp(m+1, j) + right)
            dp_table[i][j] = res
            return res
        return dp(0, n-1)
        



test = Solution()
stoneValue = [6,2,3,4,5,5]
# stoneValue = [7,7,7,7,7,7,7]
stoneValue = [2, 1, 1]
res = test.stoneGameV(stoneValue)
print(res)
        

        