from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        for i, p in enumerate(prices):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + p)
            dp_i_1 = max(dp_i_1, tmp - p)
        return dp_i_0
    
    
test = Solution()
prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
res = test.maxProfit(prices)
print(res)