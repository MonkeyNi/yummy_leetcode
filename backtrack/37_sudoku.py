from typing import List


class Solution:
    def solveNQueens(self, nums: int) -> List[List[str]]:
        
        n = 9
        def dfs(qs, row, col):
            if col == n:
                return dfs(qs, row+1, 0)
            if row == n:
                return True
            if qs[row][col] != 0:
                return dfs(qs, row, col+1)
            for i in range(1, n+1):
                if isvalid(qs, row, col, i):
                    qs[row][col] = i
                    if dfs(qs, row, col+1):
                        return True
                    qs[row][col] = 0
                else:
                    continue
            return False
            
        def isvalid(qs, r, c, target):
            # column
            for i in range(n):
                if qs[i][c] == target:
                    return False
            # row
            for i in range(n):
                if qs[r][i] == target:
                    return False
            # 3x3
            ind_r, ind_c = r//3, c//3
            for i in range(3):
                for j in range(3):
                    if qs[i+ind_r*3][j+ind_c*3] == target:
                        return False
            return True
        
        dfs(nums, 0, 0)
        return nums
    

test = Solution()
nums = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
res = test.solveNQueens(nums)
for i in res:
    print(i)
