from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]):
        # turn this problem to a '2-D maximum rectangle problem'

        def help(hs):
            res = 0
            stack = [-1]
            hs.append(0)
            for i, ele in enumerate(hs):
                while stack and ele < hs[stack[-1]]:
                    h = hs[stack.pop()]
                    w = i - stack[-1] - 1
                    res = max(res, w*h)
                stack.append(i)
            return res
        
        if not matrix or not matrix[0]:
            return 0

        res = 0
        # initialize height
        tmp = [0]*len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    tmp[j] += 1
                else:
                    tmp[j] = 0
            res = max(res, help(tmp))
        return res


test = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = []
matrix = [["0", "0"]]
res = test.maximalRectangle(matrix)
print(res)