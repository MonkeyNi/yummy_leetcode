from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        dp_i_pre_0 = 0
        for i, p in enumerate(prices):
            tmp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + p)
            dp_i_1 = max(dp_i_1, dp_i_pre_0 - p)
            dp_i_pre_0 = tmp
            
        return dp_i_0
    
    
test = Solution()
prices = [1,2,3,0,2]
# prices = [7,6,4,3,1]
res = test.maxProfit(prices)
print(res)