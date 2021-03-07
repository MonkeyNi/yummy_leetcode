from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]):
        if not edges or not edges[0]:
            return 0

        _ = float('inf')
        pathes = [[_ for i in range(n)] for j in range(n)]
        for i in range(n):
            pathes[i][i] = 0
        for e in edges:
            i, j, w = e[0]-1, e[1]-1, e[2]
            pathes[i][j] = w
            pathes[j][i] = w
        
        return pathes


test = Solution()
n = 5
edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
res = test.countRestrictedPaths(n, edges)
print(res)
            