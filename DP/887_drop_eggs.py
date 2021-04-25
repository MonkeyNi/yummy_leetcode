class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
        memo = {}
        def dp(k, n):
            """
            Args:
                k ([type]): number of good eggs
                n ([type]): number of floors need to be tested

            Returns:
                [type]: [description]
            """
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]
            res = float('inf')
            
            ## O(N * K*N)
            # for i in range(1, n+1):
            #     res = min(
            #         res, max(
            #             dp(k-1, i-1),
            #             dp(k, n-i)
            #         ) + 1
            #     )

            ## dp(k-1, i-1) and dp(k, n-i) can be regarded as functions with i as variable
            ## then it becomes a valley problem, use binary search
            ## O(N* K*logN)
            s, e = 1, n
            while s <= e:
                mid = s + (e-s)//2
                broken = dp(k-1, mid-1)
                unbroken = dp(k, n-mid)
                if broken > unbroken:
                    e = mid - 1
                    res = min(res, broken+1)
                else:
                    s = mid + 1
                    res = min(res, unbroken+1)

            memo[(k, n)] = res
            return res
        
        return dp(K, N)

    # define new function
    def superEggDrop_2(self, K: int, N: int) -> int:
        dp = [[0]*(N+1) for _ in range(K+1)]
        m = 0
        while dp[K][m] < N:
            m += 1
            for i in range(1, K+1):
                dp[i][m] = dp[i-1][m-1] + dp[i][m-1] + 1
        return m 


test = Solution()
K = 2
N = 6
res = test.superEggDrop_2(K, N)
print(res)