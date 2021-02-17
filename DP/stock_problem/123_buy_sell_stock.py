from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp = [[[0, 0] for _ in range(3)] for _ in range(len(prices))]
        
        for i in range(len(prices)):
            for k in range(2, 0, -1):
                # base cases
                if i - 1 == -1:
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue    
                if k == 0:
                    dp[i][k][0] = 0
                    dp[i][k][1] = float('-inf')
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[len(prices)-1][2][0]
    
    
test = Solution()
prices = [3,3,5,0,0,3,1,4]
prices = [1,2,3,4,5]
prices = [3,2,6,5,0,3]
res = test.maxProfit(prices)
print(res)