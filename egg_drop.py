class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # for caching
        memo = {}
        def dp(k, n):
            # if result in memo, just return
            if (k,n) in memo:
                return memo[(k, n)]
            # base case:
            if k == 1: 
                return n  # linear search
            if n == 0: 
                return 0
            
            res = float('inf')
            # list all possibles!
            """This part can be replaced by dichotomy
            """
            for i in range(1,n+1):
                res = min(
                    res, max(
                        dp(k-1, i-1),
                        dp(k, n-i)
                    ) + 1
                )

            memo[(k, n)] = res
            return res
        return dp(K, N)
        
test = Solution()
res = test.superEggDrop(10,1000)
print(res)

## TODO
## Problem: maximum recursion depth exceeded in comparison (default is 1000, code needs to be optimized)
