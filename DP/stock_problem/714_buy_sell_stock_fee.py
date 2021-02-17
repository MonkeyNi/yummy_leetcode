from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        for i, p in enumerate(prices):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + p)
            dp_i_1 = max(dp_i_1, tmp - p - fee)
        return dp_i_0
    
    
test = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2
res = test.maxProfit(prices, fee)
print(res)