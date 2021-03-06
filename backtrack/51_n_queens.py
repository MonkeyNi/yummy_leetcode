class Solution:
    """
    我这个脑子当时是怎么想出来这种解法的。把每行可能的坐标保存下来，进一步计算。
    包括位于斜线的情况下，abs(x1-x2) == abs(y1-y2).
    速度比‘标准’解法似乎快？ 主要是快在判断的部分，我这里是O（1），因为提前储存了皇后的位置
    ‘标准算法’是O（n），需要局部遍历
    """
    def solveNQueens(self, n):
        
        def dfs(path):
            """
            e.g. path = [1,2,3,4]
            """
            # avoid vertical/horizontal attack
            choices = [i for i in range(n) if not i in path]
            if not choices:
                if len(path) == n:
                    res.append(path)
                else:
                    return 
            for i in choices:
                flag = False
                # avoid slashes attack
                for j, k in enumerate(path):
                    a1, a2 = [j, k], [len(path), i]
                    if abs(a1[0]-a2[0]) == abs(a1[1]-a2[1]):
                        flag = True
                        break
                if not flag:
                    dfs(path+[i])
        
        res = []
        dfs([])
        
        # turn result to required format
        final_res = []
        for i in res:
            str_res = []
            for j in i:
                tmp = ['.']*n
                tmp[j] = 'Q'
                str_res.append("".join(tmp))
            final_res.append(str_res)
        return final_res


test = Solution()
n = 4
res = test.solveNQueens(n)
for i in res:
    print(i)
print(f'There are {len(res)} results.')