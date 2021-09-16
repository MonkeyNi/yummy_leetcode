from typing import List
import time


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return [[]]
        if n == 1:
            return [[1]]
        
        # right, down, left, up
        move_r = [0, 1, 0, -1]
        move_c = [1, 0, -1, 0]
        # initialize result
        res = [[0]*n for _ in range(n)]
        # initialize start point
        r = c = 0
        # initialize the start move direction: right
        dir = 0
        value = 1
        
        while value <= n**2:
            if 0 <= r < n and 0 <= c < n and not res[r][c]:
                res[r][c] = value
                value += 1
            else:
                # recover to inside or border
                r -= move_r[dir]
                c -= move_c[dir]
                # change direction
                dir = (dir+1)%4
            r += move_r[dir]
            c += move_c[dir]
        return res
            
            
test = Solution()
n = 3
ans = test.generateMatrix(n)
print(ans)
            