from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) <= 2 or len(board[0]) <= 2:
            return board
        
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                # start from border, change all border connect 'O' to others
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    if board[i][j] == 'O':
                        self.dfs(board, i, j)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'

        return board
        
    def dfs(self, board, i, j):
        if i < 0 or i >= len(board):
            return
        if j < 0 or j >= len(board[0]):
            return
        if board[i][j] == 'O':
            board[i][j] = '#'
            self.dfs(board, i, j-1)
            self.dfs(board, i, j+1)
            self.dfs(board, i-1, j)
            self.dfs(board, i+1, j)
        return

test = Solution()
board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
for i in board:
    print(i)
res = test.solve(board)
print('Solved: ')
for i in res:
    print(i)