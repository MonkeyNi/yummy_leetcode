from typing import List
from collections import deque

# ========== BFS ==========

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        # sorted by height
        trees = sorted((v, r, c) for (r, row) in enumerate(forest)
                       for (c, v) in enumerate(row) if v > 1)
        sr = sc = ans = 0
        for v, r, c in trees:
            d = self.getDistance(forest, sr, sc, r, c)
            if d == -1:
                return -1
            ans += d
            sr, sc = r, c
        return ans
    
    def getDistance(self, forest, sr, sc, tr, tc):
        # using bfs get the distance between two nodes
        R, C = len(forest), len(forest[0])
        visited = {(sr, sc)}
        queue = deque([(sr, sc, 0)])  # cor, distance
        while queue:
            r, c, d = queue.popleft()
            # arriived at target node, return
            if r == tr and c == tc:
                return d
            # add next 'layer'
            for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= cr < R and 0 <= cc < C and (cr, cc) not in visited and forest[cr][cc]:
                    visited.add((cr, cc))
                    queue.append((cr, cc, d+1))
        return -1
    
test = Solution()
forest = [[1,2,3],[0,0,4],[7,6,5]]
ans = test.cutOffTree(forest)
print(f'The minimum steps to cutoff all trees in descending order is {ans}')