class Solution:
    def canPartition(self, nums):
        target = sum(nums)
        if target % 2:
            return False
        
        target //= 2
        n = len(nums)
        dp = [[False for _ in range(target+1)] for _ in range(n+1)]
        dp[0][0] = True
        
        for i in range(1, n+1):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
                if j - nums[i-1] >= 0:
                    dp[i][j] = (dp[i][j] or dp[i-1][j-nums[i-1]])
        
        return dp[n][target]
        
    
    def canPartition_space_optimize(self, nums):
        """
        https://zhuanlan.zhihu.com/p/93857890
        dp[i][j] = (dp[i-1][j] or dp[i-1][j-nums[i]]), which require us tranverse in descending order.
        For 01 Knapsack problem with optimized space, we need to traverse in descending order.
        
        dp[j] = dp[j-nums[i]]  
        """
        target = sum(nums)
        if target % 2:
            return False
        
        target //= 2
        n = len(nums)
        dp = [False for _ in range(target+1)]
        dp[0] = True
        for n in nums:
            for t in range(target, 0, -1):
                if t - n >= 0:
                    dp[t] = (dp[t] or dp[t-n])
        return dp[target]