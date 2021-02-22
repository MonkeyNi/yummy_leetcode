from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        parents = {}
        sizes = {}
        
        def find(x):
            parents.setdefault(x, x)
            
            if x != parents[x]:
                parents[x] = parents[parents[x]]
                x = find(parents[x])
            return x
        
        def union(p, q):
            sizes.setdefault(q, 1)
            sizes.setdefault(p, 1)
            if sizes[p] > sizes[q]:
                parents[find(q)] = find(p)
                sizes[p] += sizes[q]
            else:
                parents[find(p)] = find(q)
                sizes[q] += sizes[p]
            
        for i in range(len(grid)):
            for j in range(len(grid)):
                if i:
                    union((i-1, j, 2), (i, j, 0))
                if j:
                    union((i, j-1, 1), (i, j, 3))
                if grid[i][j] != '/':
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 3), (i, j, 2))
                if grid[i][j] != '\\':
                    union((i, j, 0), (i, j, 3))
                    union((i, j, 1), (i, j, 2))
        return len(set(map(find, parents)))
    
    

test = Solution()
grid1 = [
  " /",
  "/ "
] # 2
grid2 = [
  " /",
  "  "
] # 1
grid3 = [
  "\\/",
  "/\\"
] # 4
grid4 = [
  "/\\",
  "\\/"
] # 5
grid5 = [
  "//",
  "/ "
] #  3
grids = [grid1, grid2, grid3, grid4, grid5]
for grid in grids:
    res = test.regionsBySlashes(grid)
    print(res)