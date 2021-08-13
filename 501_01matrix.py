class Solution:
    def updateMatrix(self, mat):
        n = len(mat)
        m = len(mat[0])
        result = [[[mat[i][j], 0] for i in range(m)] for j in range(n)]
        
        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                    tmp = []
                    for d in dirs:
                        ii = i + d[0]
                        jj = j + d[1]
                        if ii >= 0 and ii < n and jj >= 0 and jj < m:
                            tmp.append(mat[ii][jj][1])
                    result[i][j][1] = min(tmp) + 1
        res = [[result[j][i][1] for i in range(m)] for j in range(n)]
                    
        return res
    

test = Solution()
# mat = [[0,0,0],[0,1,0],[0,0,0]]
mat = [[0,0,0],[0,1,0],[1,1,1]]
print(test.updateMatrix(mat))
        