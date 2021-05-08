class Solution:
    def uniquePathsIII(self, grid):
        if not grid or not grid[0]:
            return 0
        
        # record walked grid
        log = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        # number of empty squares
        needs = sum([len([i for i in grid[j] if not i]) for j in range(len(grid))])
        w = len(grid[0])
        h = len(grid)
        res = 0
        
        def dfs(i, j, needs):
            nonlocal res
            
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in dirs:
                _i = i+d[0]
                _j = j+d[1]
                if _i < 0 or _i >= h or _j < 0 or _j >= w:
                    continue
                if grid[_i][_j] == 0 and not log[_i][_j]:
                    log[_i][_j] = True
                    needs -= 1
                    dfs(_i, _j, needs)
                    log[_i][_j] = False
                    needs += 1
                elif grid[_i][_j] == 2:
                    if needs == 0:
                        res += 1
                    # !!!
                    # do not return, all path needs to be tested
            return
        
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    dfs(i, j, needs)
        return res

test = Solution()
grid=[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
grid=[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
res = test.uniquePathsIII(grid)
print(res)