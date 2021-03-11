from typing import List
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return []
        
        res = []
        c = Counter(nums)
        
        def dfs(path, c):
            if len(path) == len(nums):
                # if I add 'if not path in res', it will takes O(n) time.
                res.append(path[:])
                return
            # traverse counter instead of nums to avoid duplicate
            for i in c:
                if c[i] > 0:
                    c[i] -= 1
                    path.append(i)
                    dfs(path, c)
                    path.pop()
                    c[i] += 1
            return
        
        dfs([], c)
        return res
    
    
test = Solution()
nums = [1, 1, 2]
res =  test.permuteUnique(nums)
print(res)
                    