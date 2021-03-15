from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def dfs(ns, path, left):
            if left < 0:
                return
            if left == 0:
                res.append(path)
                return
            for i in range(len(ns)):
                dfs(ns[i:], path+[ns[i]], left-ns[i])
            return
                    
        res = []
        dfs(candidates, [], target)
        return res
    

test = Solution()
candidates = [2,3,6,7]
target = 7
res = test.combinationSum(candidates, target)
print(res)