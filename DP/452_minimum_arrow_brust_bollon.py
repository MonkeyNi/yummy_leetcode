from typing import List

# 实际上和区间调度（435）是一个问题，只是换了一种形式

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x:x[-1])
        res = 1
        base = points[0]
        for i in range(1, len(points)):
            if points[i][0] > base[1]:
                res += 1
                base = points[i]
        return res
        
        
test = Solution()
points = [[1, 2], [1, 2]]
res = test.findMinArrowShots(points)
print(res)