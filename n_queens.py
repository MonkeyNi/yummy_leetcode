class Solution:
    def solveNQueens(self, n):
        res = []
        self.dfs([i for i in range(n)], [], res)
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


    def dfs(self, ns, path, res):
        # avoid vertical/horizontal attack
        choices = [i for i in ns if not i in path]
        if not choices:
            if len(path) == len(ns):
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
                self.dfs(ns, path+[i], res)


test = Solution()
n = 6
res = test.solveNQueens(n)
for i in res:
    print(i)
print(f'There are {len(res)} results.')