from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        dp_i_0 = 0
        dp_i_1 = float('-inf')
        for i, p in enumerate(prices):
            dp_i_0 = max(dp_i_0, dp_i_1 + p)
            dp_i_1 = max(dp_i_1, -p)
        return dp_i_0
    
    def maxProfit_2(self, prices: List[int]) -> int:
        """
        算出以每天为卖点，可以获得的利润，取最大
        """
        res = 0
        min_p = float('inf')
        for i, p in enumerate(prices):
            min_p = min(min_p, p)
            res = max(res, p - min_p)
        return res


test = Solution()
prices = [7,1,5,3,6,4]
# prices = [7,6,4,3,1]
res = test.maxProfit_2(prices)
print(res)