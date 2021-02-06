"""
This problem can be treated as find the outline of staircase
++++-
+++--
++---
++---
+----

TODO: binary search?
"""


from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        r, c, res = m-1, 0, 0
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                res += n-c
                r -= 1
            else:
                c += 1
        return res
    
print(Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))