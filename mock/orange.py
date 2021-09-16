from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        good = [(r, c) for r, row in enumerate(grid) for c, v, in enumerate(row) if v == 1]
        if not good:
            return 0
        bad = [(r, c, 0) for r, row in enumerate(grid) for c, v, in enumerate(row) if v == 2]
        if not bad:
            return -1
        # chekced = [(r, c) for r, row in enumerate(grid) for c, v, in enumerate(row) if v != 0]
        visited = set([(r, c) for r, row in enumerate(grid) for c, v, in enumerate(row) if v != 1])
        
        queue = deque()
        queue.extend(bad)
        ans = 0
        while queue:
            r, c, d = queue.popleft()
            if len(visited) == R*C:
                return ans
            for cr, cc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= cr < R and 0 <= cc < C and (cr, cc) not in visited and grid[cr][cc] == 1:
                    visited.add((cr, cc))
                    ans = max(ans, d+1)
                    queue.append((cr, cc, d+1))
        return -1


test = Solution()
grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
grid = [[0]]
grid = [[2,1,1],[1,1,1],[0,1,2]]
ans= test.orangesRotting(grid)
print(f'After {ans} minutes, there will be on good oranges.')
        