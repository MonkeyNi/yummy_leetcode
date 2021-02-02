from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [i+1 for i in range(n)]
        self.dfs(nums, k, [], res)
        return res
        # pass

    def dfs(self, nums, k, path, res):
        if len(path) == k:
            res.append(path)
        if not nums:
            return
        for i, ele in enumerate(nums):
            self.dfs(nums[i+1:],  k, path+[ele], res)

test = Solution()
n, k = 4, 3
res = test.combine(n, k)
print(res)