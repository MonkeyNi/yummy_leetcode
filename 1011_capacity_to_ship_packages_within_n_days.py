from typing import List


class Solution:
    """
    二分法特别需要注意的问题就是，起始以及结束的设置
    """
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if not weights:
            return 0
        if D == 1:
            return sum(weights)
        
        # !!!
        start, end = max(weights), sum(weights)
        
        while start <= end and end >= max(weights):
            mid = int(start + (end-start)/2)
            if self.help(weights, mid) > D:
                start = mid + 1
            else:
                end = mid - 1
        if end >= max(weights) and self.help(weights, end) <= D:
            return end
        else:
            return start
        
    def help(self, weights, n):
        pre, res = 0, 0
        for i, ele in enumerate(weights):
            pre += ele
            if pre > n:
                res += 1
                pre = ele
            if i == len(weights)-1 and pre <= n:
                res += 1      
        return res
        

test = Solution()
weights = [1,2,3,4,5,6,7,8,9,10]
D = 5
# weights = [3,2,2,4,1,4]
# D = 3
# weights = [1,2,3,1,1]
# D = 4
res = test.shipWithinDays(weights, D)
print(res)