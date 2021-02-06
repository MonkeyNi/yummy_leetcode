from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]):
        if not nums:
            return []
        res = []
        for i, ele in enumerate(nums):
            ind = bisect_left(res, ele)
            if ind == len(res):
                res.append(ele)
            else:
                res[ind] = ele

        return len(res)


test = Solution()
nums = [0,1,0,3,2,3]
res = test.lengthOfLIS(nums)
print(res)