from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(ns, path):
            if len(path) == k:
                res.append(path)
            for i, ele in enumerate(ns):
                dfs(ns[i+1:], path+[ele])
        
        res = []
        ns = [i for i in range(1, n+1)]
        dfs(ns, [])
        return res

test = Solution()
n, k = 4, 3
res = test.combine(n, k)
print(res)