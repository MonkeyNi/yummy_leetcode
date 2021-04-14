from typing import List
import numpy as np


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        r = len(grid)
        c = len(grid[0])
        visited = [[False for _  in range(c)] for _ in range(r)]
        res = 0
        
        def help(grid, sr, sc):
            nonlocal res
            if not inarea(sr, sc):
                return 0
            if visited[sr][sc]:
                return 1
            if grid[sr][sc] != 1:
                return 0
            visited[sr][sc] = True
            
            surround = (help(grid, sr-1, sc) + help(grid, sr+1, sc) + help(grid, sr, sc-1) + help(grid, sr, sc+1))
            res += (4 - surround)
            return 1
        
        def inarea(sr, sc):
            if sr < r and sr >= 0 and sc < c  and sc >= 0:
                return True
            return False

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1: 
                    help(grid, i, j)
                    return res
    

test = Solution()
grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# grid = [[1]]
res = test.islandPerimeter(grid)
print(res)