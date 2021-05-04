from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        
        k = min(len(prices)//2, k)
        dp = [[[0, 0] for _ in range(k+1)] for _ in range(len(prices))]
        
        for i in range(len(prices)):
            for kk in range(k, -1, -1):
                # base cases
                if i - 1 == -1:
                    dp[i][kk][0] = 0
                    dp[i][kk][1] = -prices[i] # i==0 instead of -1, so dp[0][kk][1] = max(float('-inf'), -price[i])
                    continue    
                if kk == 0:
                    dp[i][kk][0] = 0
                    dp[i][kk][1] = float('-inf')
                    continue
                dp[i][kk][0] = max(dp[i-1][kk][0], dp[i-1][kk][1] + prices[i])
                dp[i][kk][1] = max(dp[i-1][kk][1], dp[i-1][kk-1][0] - prices[i])
        return dp[len(prices)-1][k][0]
    
    
test = Solution()
k = 2
prices = [2,4,1]
# k = 2
# prices = [3,2,6,5,0,3]
# k = 2
# prices = [3,3,5,0,0,3,1,4]
res = test.maxProfit(k, prices)
print(res)
print(test.maxProfit_2(k, prices))