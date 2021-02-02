from typing import List


class Solution:
    # Backtracking
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        res.append(path)
        if not nums:
            return
        for i, ele in enumerate(nums):
            self.dfs(nums[i+1:], path+[ele], res)
    
    # Mathematical induction
    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return None
        res = [[]]
        for i in nums:
            res.extend([ele+[i] for ele in res])
        return res

test = Solution()
nums = [1,2,3,4]
res = test.subsets_2(nums)
for i in res:
    print(i)

import math
assert (len(res) == math.pow(2, len(nums)))