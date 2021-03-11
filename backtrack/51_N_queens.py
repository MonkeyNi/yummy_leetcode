from typing import List
import copy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def dfs(qs, row):
            if row == n:
                # If just use res.append(qs), I will get wrong answer
                # since qs will be changed later
                res.append(copy.deepcopy(qs))
            for i in range(n):
                if isvalid(qs, row, i):
                    qs[row][i] = 'Q'
                    dfs(qs, row+1)
                    qs[row][i] = '.'
        
        def isvalid(qs, r, c):
            # column
            for i in range(n):
                if qs[i][c] == 'Q':
                    return False
            # right top
            for i, j in zip(range(r-1, -1, -1), range(c+1, n)):
                if qs[i][j] == 'Q':
                    return False
            
            # left top
            for i, j in zip(range(r-1, -1, -1), range(c-1, -1, -1)):
                if qs[i][j] == 'Q':
                    return False 
            return True
        
        
        res = []
        qs = [['.' for _ in range(n)] for _ in range(n)]
        dfs(qs, 0)
        
        res = list(map(list, [("".join(t) for t in b)  for b in res]))
        return res
    

test = Solution()
n = 4
res = test.solveNQueens(4)
print(res)